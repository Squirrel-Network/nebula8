from core import decorators
from core.utilities.message import message
from languages.getLang import languages
from core.database.repository.group import GroupRepository
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.utilities.menu import build_menu

@decorators.admin.user_admin
@decorators.delete.init
def init(update, context):
    languages(update,context)
    record = GroupRepository.SET_WELCOME_TEXT
    chat = update.effective_chat.id
    msg = update.message.text[8:].strip()
    if msg != "":
        data = [(msg, chat)]
        GroupRepository().update_group_settings(record, data)
        message(update, context, languages.set_welcome_help)
    else:
        message(update, context, languages.set_welcome_main)


@decorators.admin.user_admin
@decorators.delete.init
def set_type_no_username(update, context):
    bot = context.bot
    chat = update.effective_message.chat_id
    buttons = []
    buttons.append(InlineKeyboardButton('Kick Only', callback_data='tpnu1'))
    buttons.append(InlineKeyboardButton('Message Only', callback_data='tpnu2'))
    buttons.append(InlineKeyboardButton('Mute Only', callback_data='tpnu3'))
    menu = build_menu(buttons,3)
    bot.send_message(chat,"No Username Filter Settings", reply_markup=InlineKeyboardMarkup(menu),parse_mode='HTML')


@decorators.admin.user_admin
def update_set_tpnu(update, context):
    query = update.callback_query
    if query.data.startswith("tpnu"):
        chat_id = query.message.chat_id
        tpnu_set = query.data[4:]
        record = GroupRepository.SET_TPNU
        data = [(tpnu_set,chat_id)]
        GroupRepository().update_group_settings(record, data)
        text = "You have set the filter to <code>{}</code>\nLegend:\n<code>1 == Kick\n2 == Message\n3 == Mute</code>".format(tpnu_set)
        query.edit_message_text(text, parse_mode='HTML')