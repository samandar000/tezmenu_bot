from flask import Flask,request
import os
from telegram.ext import(
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler,
    Dispatcher
)

from main import(start,catalog,order,cart,userinfo,administration,users,welcome_text,cancel,bonus_rate,notaviable,addresses,addaddresses,accept,placeorder,clear)

app = Flask(__name__)

TOKEN = os.environ['TOKEN']
updater = Updater(token=TOKEN)

@app.route('/webhook', methods=['POST','GET'])
def webhook():
    
    if request.method == 'GET':
        return 'hi from Python-2022I'
    elif request.method == 'POST':
        
        # dp: Dispatcher = Dispatcher(None,workers=0)

        updater.dispatcher.add_handler(CommandHandler('start', start))
        updater.dispatcher.add_handler(MessageHandler(Filters.text('🏬 Catalog'),catalog))
        updater.dispatcher.add_handler(MessageHandler(Filters.text('📦 Orders'),order))
        updater.dispatcher.add_handler(MessageHandler(Filters.text('🛒 Cart'),cart))
        updater.dispatcher.add_handler(MessageHandler(Filters.text('👤 User info'),userinfo))
        updater.dispatcher.add_handler(MessageHandler(Filters.text('🎛 Administration'),administration))
        updater.dispatcher.add_handler(MessageHandler(Filters.text('🚪 Exit'),start))
        updater.dispatcher.add_handler(MessageHandler(Filters.text('👥 Users'),users))
        updater.dispatcher.add_handler(MessageHandler(Filters.text('👋 Welcome text'),welcome_text))
        updater.dispatcher.add_handler(MessageHandler(Filters.text('❌ Cancel'),administration))
        updater.dispatcher.add_handler(MessageHandler(Filters.text('🤑 Bonus rate'),bonus_rate))
        updater.dispatcher.add_handler(MessageHandler(Filters.text('➕ Add category'),notaviable))
        updater.dispatcher.add_handler(MessageHandler(Filters.text('📦 New product'),notaviable))
        updater.dispatcher.add_handler(MessageHandler(Filters.text('🗑 Remove category'),notaviable))
        updater.dispatcher.add_handler(MessageHandler(Filters.text('🗑 Delete product'),notaviable))


        updater.dispatcher.add_handler(CallbackQueryHandler(addaddresses,pattern='add'))
        updater.dispatcher.add_handler(CallbackQueryHandler(addresses,pattern='iplace'))
        updater.dispatcher.add_handler(CallbackQueryHandler(accept,pattern='accept'))
        updater.dispatcher.add_handler(CallbackQueryHandler(cancel,pattern='cancel'))
        updater.dispatcher.add_handler(CallbackQueryHandler(placeorder,pattern='placeorder'))
        updater.dispatcher.add_handler(CallbackQueryHandler(clear,pattern='clear'))



        return 'Hello'