import os
import sys
sys.path.insert(0, 'src')

from rag.queryHandler import getResponse
from indexing.chromaSetup import createVectorStore
from bot.telegramBot import setupBot

def main():
    print('🔄 Carregando documentos...')
    vectorStore = createVectorStore()
    retriever = vectorStore.as_retriever()
    
    print('✅ Iniciando bot...')
    app = setupBot(os.getenv('TELEGRAM_TOKEN'), retriever, getResponse)
    app.run_polling()

if __name__ == '__main__':
    main()