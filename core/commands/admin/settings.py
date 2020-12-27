from core import decorators
from core.utilities.menu import build_menu
from languages.getLang import languages
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.database.repository.group import GroupRepository
from telegram.ext import CallbackQueryHandler

def keyboard_settings(update,context,editkeyboard = False):
    bot = context.bot
    chat = update.message.chat_id
    group = GroupRepository().getById(chat)
    list_buttons = []
    list_buttons.append(InlineKeyboardButton('Welcome %s' % ('✅' if group['set_welcome'] == 1 else '❌'), callback_data='setWelcome'))
    list_buttons.append(InlineKeyboardButton("Close", callback_data='close'))
    menu = build_menu(list_buttons,2)
    if editkeyboard == False:
        keyboard_menu = bot.send_message(chat,"Group Settings",reply_markup=InlineKeyboardMarkup(menu),parse_mode='HTML')
    if editkeyboard == True:
        keyboard_menu = bot.edit_message_reply_markup(chat,update.message.message_id,reply_markup=InlineKeyboardMarkup(menu))
    return keyboard_menu

@decorators.admin.user_admin
def init(update,context):
    keyboard_settings(update,context)

@decorators.admin.user_admin
def update_settings(update,context):
    query = update.callback_query
    chat = update.effective_message.chat_id
    group = GroupRepository().getById(chat)
    if query.data == 'setWelcome':
        row = group['set_welcome']
        if row == 1:
            data = [(0,chat)]
            GroupRepository().SetWelcome(data)
            return keyboard_settings(query,context,True)
        else:
            data = [(1,chat)]
            GroupRepository().SetWelcome(data)
            return keyboard_settings(query,context,True)
    if query.data == 'close':
        query.edit_message_text("You have closed the settings menu",parse_mode='HTML')