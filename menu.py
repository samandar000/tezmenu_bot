from telegram.ext import(
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler
)
from telegram import KeyboardButton,ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup
def start(update,context):
    chat_id = update.message.chat.id
    bot = context.bot

    bot.sendMessage(chat_id,'Hello! 👋 This is a demo version of the Telegram Store bot. You can test out catalog function and checkout process.')


def echo(update,context):
    chat_id = update.message.chat.id
    text = update.message.text
    bot = context.bot
    
    catalog = KeyboardButton(text='🏬Catalog')
    order = KeyboardButton(text='📦Order')
    userinfo = KeyboardButton(text='👤User info')
    cart = KeyboardButton(text='🛒Cart')
    administration = KeyboardButton(text='🎛Administration')

    keyboard = ReplyKeyboardMarkup(
        [
            [catalog,order],
            [userinfo,cart],
            [administration]
        ],
        resize_keyboard=True)
    
    bot.sendMessage(chat_id,text,reply_markup = keyboard)

def inlinekeyboard(update, context):
    chat_id = update.message.chat.id
    text = update.message.text
    bot = context.bot

    pizza = InlineKeyboardButton(
        text='pizza🍕',
        callback_data='pizza'
        )
    keyboard = InlineKeyboardButton([[pizza]])
    text = '🏬Catalog'
    
    bot.sendMessage(chat_id,text=text,reply_murkup = keyboard )

def catalog(update,context):
    print(1)
    query = update.callback_query
    catalog = InlineKeyboardButton(
        text='🍕 pizza',
        switch_inline_query_current_chat='🍕 pizza'
    )
    reply_markup = InlineKeyboardMarkup(
        [
            [catalog]
        ]
    )
    update.message.reply_text(text='🏬 Catalog',reply_markup=reply_markup)
updater = Updater('5643654386:AAGaxNP-8Kkwzi8Ko047p0BZBd3t6a0eIu4')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🏬 Catalog'),catalog))
# updater.dispatcher.add_handler(MessageHandler(Filters.text('👤 Userinfo'),userinfo))
# updater.dispatcher.add_handler(MessageHandler(Filters.text('🎛 Administration'),administration))
updater.start_polling()
updater.idle()