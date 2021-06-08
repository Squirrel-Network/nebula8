from core.utilities.menu import build_menu
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def init(update,context):
    bot = context.bot
    chat = update.effective_message.chat_id
    msg = "Hi my name is {}\nDo You need Help?".format("@"+bot.username)
    buttons = []
    buttons.append(InlineKeyboardButton("Commands List", url='https://github.com/Squirrel-Network/nebula8/wiki/Command-List'))
    buttons.append(InlineKeyboardButton("Source", url='https://github.com/Squirrel-Network/nebula8'))
    buttons.append(InlineKeyboardButton("Logs Channel", url='https://t.me/nebulalogs'))
    buttons.append(InlineKeyboardButton("News Channel", url='https://t.me/nebulanewsbot'))
    buttons.append(InlineKeyboardButton("BlackList Search", url='https://squirrel-network.online/knowhere'))
    buttons.append(InlineKeyboardButton("Official API Docs", url='https://api.nebula.squirrel-network.online/apidocs'))
    menu = build_menu(buttons,2)
    bot.send_message(chat,msg,reply_markup=InlineKeyboardMarkup(menu))