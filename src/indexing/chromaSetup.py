from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_aws import BedrockEmbeddings
from langchain_community.vectorstores import Chroma
from utils.awsConfig import getS3Client

def createVectorStore():
    print("📁 Modo local - Usando arquivos de exemplo")
    
    # 1. Tenta carregar de arquivos locais se existirem
    documents = []
    if os.path.exists('/app/data/'):
        for file in os.listdir('/app/data/'):
            if file.endswith('.pdf'):
                loader = PyPDFLoader(f'/app/data/{file}')
                documents.extend(loader.load())
    
    # 2. Se não achou arquivos, usa dados de exemplo
    if not documents:
        from langchain.docstore.document import Document
        documents = [
            Document(page_content="Lei de Introdução às Normas do Direito Brasileiro."),
            Document(page_content="Código Civil. Art. 1º: Toda pessoa é capaz de direitos e deveres."),
        ]
        print("⚠️  Usando dados de exemplo")
    
    textSplitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = textSplitter.split_documents(documents)
    
    embeddings = BedrockEmbeddings(region_name='us-east-1', model_id='amazon.titan-embed-text-v1')
    return Chroma.from_documents(chunks, embeddings, persist_directory='/app/chromaDb')