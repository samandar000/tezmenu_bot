from telegram.ext import(
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler
)
from telegram import KeyboardButton,ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup
def start(update,context):
    text = 'Hello! ๐ \nThis is a demo version of the Telegram Store bot. You can test out catalog function and checkout process.'
    bot = context.bot
    
    Catalog = KeyboardButton(text='๐ฌ Catalog')
    Orders = KeyboardButton(text='๐ฆ Orders')
    Userinfo = KeyboardButton(text='๐ค User info')
    Cart = KeyboardButton(text='๐ Cart')
    Administration = KeyboardButton(text='๐ Administration')

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
        text='๐ pizza',
        switch_inline_query_current_chat='๐ pizza'
    )
    reply_markup = InlineKeyboardMarkup(
        [
            [catalog]
        ]
    )
    update.message.reply_text(text = '๐ฌ Catalog',reply_markup = reply_markup)

def order(update,context):
    cancel = InlineKeyboardButton(
        text='โ Cancel',
        callback_data='cancel'
    )
    accept = InlineKeyboardButton(
        text='โ Accept',
        callback_data='accept'
    )
    keyboard = InlineKeyboardMarkup(
        [
            [accept,cancel]
        ]
    )   
    text='๐ฆ Your order\n\nChili Pizza (14") - $22.99 x1 = $22.99\n\n๐ต Amount to pay: $22.99\n\n๐ฌ Comment to the order: ๐ฆ Orders'
    update.message.reply_text(text,reply_markup = keyboard)

def cart(update,context):
    place_order = InlineKeyboardButton(
        text= 'โ Place order',
        callback_data='placeorder'
    )
    clear = InlineKeyboardButton(
        text='๐งน Clear',
        callback_data='clear'
    )
    keyboard = InlineKeyboardMarkup(
        [
            [place_order,clear]
        ]
    )
    text = '๐ Cart\n\nChili Pizza (14") - $22.99 x1 = $22.99\n\n๐ต Total: $22.99'
    update.message.reply_text(text,reply_markup = keyboard)
def userinfo(update,context):
    bot = context.bot
    query = update.callback_query
    chat_id = update.message.chat.id
    first_name = update.message.from_user.first_name
    addresses = InlineKeyboardButton(
        text='๐? Addresses',
        callback_data='iplace'
    )
    add_address = InlineKeyboardButton(
        text= 'โ Add address',
        callback_data='add'
    )
    keyboard = InlineKeyboardMarkup(
        [
            [addresses,add_address]
        ],resize_keyboard=True
    )
    text = f'๐ค {first_name}\n๐ค Invited friends: 0\n๐ธ Bonus balance: $0.0\nโน๏ธ You can get 5.0% on your bonus balance from the amount of each order of your invited friends.'
    bot.sendMessage(chat_id,text=text,reply_markup = keyboard)
def administration(update,context):
    users = KeyboardButton(text= '๐ฅ Users')
    orders = KeyboardButton(text= '๐ท Orders')
    welcome_text = KeyboardButton(text='๐ Welcome text')
    bonus = KeyboardButton(text='๐ค Bonus rate')
    add = KeyboardButton(text='โ Add category')
    remove = KeyboardButton(text='๐ Remove category')
    new = KeyboardButton(text='๐ฆ New product')
    delete = KeyboardButton(text='๐ Delete product')
    exit = KeyboardButton(text='๐ช Exit')

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
    cancel = KeyboardButton(text='โ Cancel')

    keyboard = ReplyKeyboardMarkup(
        [
            [cancel]
        ],
        resize_keyboard=True
    )
    text = '๐ New welcome text Send the text of greeting in one message.You can use Telegram Markdown to format your message:*bold text* _italic text_'
    update.message.reply_text(text,reply_markup = keyboard)
def cancel(update,context):
    query = update.callback_query
    query.edit_message_text(text = 'โ Order cancelled') 
def bonus_rate(update,context):
    cancel = KeyboardButton(text='โ Cancel')

    keyboard = ReplyKeyboardMarkup(
        [
            [cancel]
        ],
        resize_keyboard=True
        
    )
    text = '๐ค Bonus rate'
    update.message.reply_text(text,reply_markup = keyboard)
def notaviable(update,context):
    Users = KeyboardButton(text='๐ฅ Users')
    Orders = KeyboardButton(text='๐ท Orders')
    Welcome = KeyboardButton(text='๐ Welcome text')
    Bonus = KeyboardButton(text='๐ค Bonus rate')
    Add = KeyboardButton(text='โ Add category')
    Remove = KeyboardButton(text='๐ Remove category')
    New = KeyboardButton(text='๐ฆ New product')
    Delete = KeyboardButton(text='๐ Delete product')
    Exit = KeyboardButton(text='๐ช Exit')
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
    text = 'โก๏ธ Not available in demo version.'
    update.message.reply_text(text,reply_markup=keyboard)
def addresses(update,context):
    query = update.callback_query
    bot = context.bot
    chat_id = update.callback_query.message.chat.id
    text = ' Please send the address to which you want your order to be delivered.'
    location = KeyboardButton(
        text = '๐ Location',
        request_location=True
    )
    cancel = KeyboardButton(text = '๐ช Exit')
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
    text ='๐ Please send the address to which you want your order to be delivered.'
    bot = context.bot 
    query = update.callback_query
    chat_id = update.callback_query.message.chat.id 
    bot.sendMessage(chat_id,text=text)
    query.answer(text='Working...')
def accept(update,context):
    query = update.callback_query
    bot = context.bot
    chat_id = update.callback_query.message.chat.id
    text1 = '๐ฆ Your order\n\nChili Pizza (14") - $22.99 x1 = $22.99\n\n๐ต Amount to pay: $22.99\n\n๐ฌ Comment to the order: ๐ฆ Orders'
    text2= 'โ Order placed!'
    query.edit_message_text(text1)
    bot.sendMessage(chat_id,text=text2)
def cancel(update,context):
    query = update.callback_query
    query.edit_message_text(text='โ Order cancelled')
def placeorder(update,context):
    query = update.callback_query
    bot = context.bot
    chat_id = update.callback_query.message.chat.id
    text = '๐ Choose shipping address:'
    location = KeyboardButton(
        text = '๐ Location',
        request_location=True
    )
    cancel = KeyboardButton(text='๐ช Exit')
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
    query.edit_message_text(text='โ Cart cleared')
updater = Updater('5643654386:AAGaxNP-8Kkwzi8Ko047p0BZBd3t6a0eIu4')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('๐ฌ Catalog'),catalog))
updater.dispatcher.add_handler(MessageHandler(Filters.text('๐ฆ Orders'),order))
updater.dispatcher.add_handler(MessageHandler(Filters.text('๐ Cart'),cart))
updater.dispatcher.add_handler(MessageHandler(Filters.text('๐ค User info'),userinfo))
updater.dispatcher.add_handler(MessageHandler(Filters.text('๐ Administration'),administration))
updater.dispatcher.add_handler(MessageHandler(Filters.text('๐ช Exit'),start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('๐ฅ Users'),users))
updater.dispatcher.add_handler(MessageHandler(Filters.text('๐ Welcome text'),welcome_text))
updater.dispatcher.add_handler(MessageHandler(Filters.text('โ Cancel'),administration))
updater.dispatcher.add_handler(MessageHandler(Filters.text('๐ค Bonus rate'),bonus_rate))
updater.dispatcher.add_handler(MessageHandler(Filters.text('โ Add category'),notaviable))
updater.dispatcher.add_handler(MessageHandler(Filters.text('๐ฆ New product'),notaviable))
updater.dispatcher.add_handler(MessageHandler(Filters.text('๐ Remove category'),notaviable))
updater.dispatcher.add_handler(MessageHandler(Filters.text('๐ Delete product'),notaviable))


updater.dispatcher.add_handler(CallbackQueryHandler(addaddresses,pattern='add'))
updater.dispatcher.add_handler(CallbackQueryHandler(addresses,pattern='iplace'))
updater.dispatcher.add_handler(CallbackQueryHandler(accept,pattern='accept'))
updater.dispatcher.add_handler(CallbackQueryHandler(cancel,pattern='cancel'))
updater.dispatcher.add_handler(CallbackQueryHandler(placeorder,pattern='placeorder'))
updater.dispatcher.add_handler(CallbackQueryHandler(clear,pattern='clear'))

updater.start_polling()
updater.idle()