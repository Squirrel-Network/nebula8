from telegram import InlineKeyboardButton, InlineKeyboardMarkup

HELP_KEYBOARD = [[
    InlineKeyboardButton("Commands List", url='https://github.com/Squirrel-Network/nebula8/wiki/Command-List'),
    InlineKeyboardButton("Source", url='https://github.com/Squirrel-Network/nebula8'),
    InlineKeyboardButton("BlackList Search", url='https://squirrel-network.online/knowhere/')
    ]]

def init(update,context):
    bot = context.bot
    chat = update.effective_message.chat_id
    msg = "Do You need Help?"
    reply_markup = InlineKeyboardMarkup(HELP_KEYBOARD)
    bot.send_message(chat,msg,reply_markup=reply_markup)