from telegram.ext import(
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler
)
from telegram import KeyboardButton,ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup
def start(update,context):
    text = 'Hello! 👋 \nThis is a demo version of the Telegram Store bot. You can test out catalog function and checkout process.'
    bot = context.bot
    
    Catalog = KeyboardButton(text='🏬 Catalog')
    Orders = KeyboardButton(text='📦 Orders')
    Userinfo = KeyboardButton(text='👤 User info')
    Cart = KeyboardButton(text='🛒 Cart')
    Administration = KeyboardButton(text='🎛 Administration')

    keyboard = ReplyKeyboardMarkup(
        [
            [Catalog,Orders],
            [Userinfo,Cart],
            [Administration]
        ],
        resize_keyboard=True
    )
    update.message.reply_text(text=text,reply_markup = keyboard)
def catalog(update,context):
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
    update.message.reply_text(text = '🏬 Catalog',reply_markup = reply_markup)

def order(update,context):
    cancel = InlineKeyboardButton(
        text='❌ Cancel',
        callback_data='cancel'
    )
    accept = InlineKeyboardButton(
        text='✅ Accept',
        callback_data='accept'
    )
    keyboard = InlineKeyboardMarkup(
        [
            [accept,cancel]
        ]
    )   
    text='📦 Your order\n\nChili Pizza (14") - $22.99 x1 = $22.99\n\n💵 Amount to pay: $22.99\n\n💬 Comment to the order: 📦 Orders'
    update.message.reply_text(text,reply_markup = keyboard)

def cart(update,context):
    place_order = InlineKeyboardButton(
        text= '✅ Place order',
        callback_data='placeorder'
    )
    clear = InlineKeyboardButton(
        text='🧹 Clear',
        callback_data='clear'
    )
    keyboard = InlineKeyboardMarkup(
        [
            [place_order,clear]
        ]
    )
    text = '🛒 Cart\n\nChili Pizza (14") - $22.99 x1 = $22.99\n\n💵 Total: $22.99'
    update.message.reply_text(text,reply_murkup = keyboard)
updater = Updater('5643654386:AAGaxNP-8Kkwzi8Ko047p0BZBd3t6a0eIu4')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🏬 Catalog'),catalog))
updater.dispatcher.add_handler(MessageHandler(Filters.text('📦 Orders'),order))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🛒 Cart'),cart))






updater.start_polling()
updater.idle()