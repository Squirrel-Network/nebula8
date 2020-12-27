from core import decorators
from core.utilities.menu import build_menu
from languages.getLang import languages
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.database.repository.group import GroupRepository

#TODO Devo poter tornare la funzione keyboard_settings al posto di query.edit... per un menu dinamico in tempo reale.
def keyboard_settings(update,context):
    bot = context.bot
    chat = update.effective_message.chat_id
    group = GroupRepository().getById(chat)
    list_buttons = []
    list_buttons.append(InlineKeyboardButton('Welcome %s' % ('✅' if group['set_welcome'] == 1 else '❌'), callback_data='setWelcome'))
    list_buttons.append(InlineKeyboardButton("Close", callback_data='close'))
    menu = build_menu(list_buttons,2)
    keyboard_menu = bot.send_message(chat,"Group Settings",reply_markup=InlineKeyboardMarkup(menu),parse_mode='HTML')
    #keyboard_menu = update.message.reply_text("Group Settings",reply_markup=InlineKeyboardMarkup(menu),parse_mode='HTML')
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
            query.edit_message_text("You have set welcome to off",parse_mode='HTML')
        else:
            data = [(1,chat)]
            GroupRepository().SetWelcome(data)
            query.edit_message_text("You have set welcome to active",parse_mode='HTML')
        #return keyboard_settings(query,context)
    if query.data == 'close':
        query.edit_message_text("You have closed the settings menu",parse_mode='HTML')