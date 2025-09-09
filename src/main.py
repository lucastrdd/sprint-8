import os
from src.indexing.chromaSetup import createVectorStore
from src.rag.queryHandler import getResponse
from src.bot.telegramBot import setupBot

def main():
    print('🔄 Carregando documentos...')
    vectorStore = createVectorStore()
    retriever = vectorStore.as_retriever()
    
    print('✅ Iniciando bot...')
    app = setupBot(os.getenv('TELEGRAM_TOKEN'), retriever, getResponse)
    app.run_polling()

if __name__ == '__main__':
    main()