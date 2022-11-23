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
    update.message.reply_text(text,reply_markup = keyboard)
def userinfo(update,context):
    bot = context.bot
    query = update.callback_query
    chat_id = update.message.chat.id
    first_name = update.message.from_user.first_name
    addresses = InlineKeyboardButton(
        text='🏠 Addresses',
        callback_data='iplace'
    )
    add_address = InlineKeyboardButton(
        text= '➕ Add address',
        callback_data='add'
    )
    keyboard = InlineKeyboardMarkup(
        [
            [addresses,add_address]
        ],resize_keyboard=True
    )
    text = f'👤 {first_name}\n🤝 Invited friends: 0\n💸 Bonus balance: $0.0\nℹ️ You can get 5.0% on your bonus balance from the amount of each order of your invited friends.'
    bot.sendMessage(chat_id,text=text,reply_markup = keyboard)
def administration(update,context):
    users = KeyboardButton(text= '👥 Users')
    orders = KeyboardButton(text= '🏷 Orders')
    welcome_text = KeyboardButton(text='👋 Welcome text')
    bonus = KeyboardButton(text='🤑 Bonus rate')
    add = KeyboardButton(text='➕ Add category')
    remove = KeyboardButton(text='🗑 Remove category')
    new = KeyboardButton(text='📦 New product')
    delete = KeyboardButton(text='🗑 Delete product')
    exit = KeyboardButton(text='🚪 Exit')

    keyboard = ReplyKeyboardMarkup(
        [
            [users,orders],
            [welcome_text,bonus],
            [add,remove],
            [new,delete],
            [exit]
        ],
        resize_keyboard=True
    )
    text = update.message.text
    update.message.reply_text(text,reply_markup=keyboard)
def users(update,context):
    update.message.reply_text(text='No users')
def welcome_text(update,context):
    cancel = KeyboardButton(text='❌ Cancel')

    keyboard = ReplyKeyboardMarkup(
        [
            [cancel]
        ],
        resize_keyboard=True
    )
    text = '👋 New welcome text Send the text of greeting in one message.You can use Telegram Markdown to format your message:*bold text* _italic text_'
    update.message.reply_text(text,reply_markup = keyboard)
def cancel(update,context):
    query = update.callback_query
    query.edit_message_text(text = '❌ Order cancelled') 
def bonus_rate(update,context):
    cancel = KeyboardButton(text='❌ Cancel')

    keyboard = ReplyKeyboardMarkup(
        [
            [cancel]
        ],
        resize_keyboard=True
        
    )
    text = '🤑 Bonus rate'
    update.message.reply_text(text,reply_markup = keyboard)
def notaviable(update,context):
    Users = KeyboardButton(text='👥 Users')
    Orders = KeyboardButton(text='🏷 Orders')
    Welcome = KeyboardButton(text='👋 Welcome text')
    Bonus = KeyboardButton(text='🤑 Bonus rate')
    Add = KeyboardButton(text='➕ Add category')
    Remove = KeyboardButton(text='🗑 Remove category')
    New = KeyboardButton(text='📦 New product')
    Delete = KeyboardButton(text='🗑 Delete product')
    Exit = KeyboardButton(text='🚪 Exit')
    keyboard = ReplyKeyboardMarkup(
        [
            [Users,Orders],
            [Welcome,Bonus],
            [Add,Remove],
            [New,Delete],
            [Exit]
        ],
        resize_keyboard=True
    )
    text = '⚡️ Not available in demo version.'
    update.message.reply_text(text,reply_markup=keyboard)
def addresses(update,context):
    query = update.callback_query
    bot = context.bot
    chat_id = update.callback_query.message.chat.id
    text = ' Please send the address to which you want your order to be delivered.'
    location = KeyboardButton(
        text = '📍 Location',
        request_location=True
    )
    cancel = KeyboardButton(text = '🚪 Exit')
    keyboard = ReplyKeyboardMarkup(
        [
            [location],
            [cancel]
        ],
        resize_keyboard=True
    )
    bot.sendMessage(chat_id,text=text,reply_markup=keyboard)
    
    query.answer('Working...')
def addaddresses(update,context):
    text ='📍 Please send the address to which you want your order to be delivered.'
    bot = context.bot 
    query = update.callback_query
    chat_id = update.callback_query.message.chat.id 
    bot.sendMessage(chat_id,text=text)
    query.answer(text='Working...')
def accept(update,context):
    query = update.callback_query
    bot = context.bot
    chat_id = update.callback_query.message.chat.id
    text1 = '📦 Your order\n\nChili Pizza (14") - $22.99 x1 = $22.99\n\n💵 Amount to pay: $22.99\n\n💬 Comment to the order: 📦 Orders'
    text2= '✅ Order placed!'
    query.edit_message_text(text1)
    bot.sendMessage(chat_id,text=text2)
def cancel(update,context):
    query = update.callback_query
    query.edit_message_text(text='❌ Order cancelled')
def placeorder(update,context):
    query = update.callback_query
    bot = context.bot
    chat_id = update.callback_query.message.chat.id
    text = '📍 Choose shipping address:'
    location = KeyboardButton(
        text = '📍 Location',
        request_location=True
    )
    cancel = KeyboardButton(text='🚪 Exit')
    keyboard = ReplyKeyboardMarkup(
        [
            [location],
            [cancel]
        ],
        resize_keyboard=True
    )
    bot.sendMessage(chat_id,text=text,reply_markup=keyboard)
    query.answer('Waiting...')
def clear(update,context):
    query = update.callback_query
    query.edit_message_text(text='✅ Cart cleared')
updater = Updater('5643654386:AAGaxNP-8Kkwzi8Ko047p0BZBd3t6a0eIu4')

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

updater.start_polling()
updater.idle()