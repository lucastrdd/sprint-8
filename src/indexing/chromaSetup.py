import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_aws import BedrockEmbeddings
from langchain_community.vectorstores import Chroma
from src.utils.awsConfig import getS3Client

def createVectorStore():
    s3Client = getS3Client()
    embeddings = BedrockEmbeddings(
        region_name="us-east-1",
        model_id="amazon.titan-embed-text-v1"
    )
    
    documents = []
    result = s3Client.list_objects_v2(
        Bucket='chatbot-lucas-dataset-202509',  
        Prefix='dataset/juridicos/'
    )
    
    for obj in result['Contents']:
        if obj['Key'].endswith('.pdf'):
            print(f"📄 Processando: {obj['Key']}")
            presignedUrl = s3Client.generate_presigned_url(
                'get_object',
                Params={
                    'Bucket': 'chatbot-lucas-dataset-202509',
                    'Key': obj['Key']
                },
                ExpiresIn=300
            )
            loader = PyPDFLoader(presignedUrl)
            documents.extend(loader.load())
    
    textSplitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )
    chunks = textSplitter.split_documents(documents)
    
    return Chroma.from_documents(
        chunks, 
        embeddings, 
        persist_directory='/app/chromaDb'
    )