from src.llm.bedrockClient import getLlm
from langchain.chains import RetrievalQA

def getResponse(retriever, question):
    llm = getLlm()
    qaChain = RetrievalQA.from_chain_type(llm=llm, chain_type='stuff', retriever=retriever)
    return qaChain.invoke({'query': question})['result']