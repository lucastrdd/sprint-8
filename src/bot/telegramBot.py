from telegram.ext import Application, CommandHandler, MessageHandler, filters

def setupBot(token, retriever, ragHandler):
    app = Application.builder().token(token).build()
    
    async def start(update, context):
        await update.message.reply_text('Assistente jurídico pronto! Faça sua pergunta.')
    
    async def handleMessage(update, context):
        response = ragHandler(retriever, update.message.text)
        await update.message.reply_text(response)
    
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT, handleMessage))
    
    return app