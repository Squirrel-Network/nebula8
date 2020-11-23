from core import decorators
from core.database.repository.group import GroupRepository
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

LANGUAGE_KEYBOARD = [[
    InlineKeyboardButton("EN", callback_data='language_en'),
    InlineKeyboardButton("IT", callback_data='language_it')
    ]]

@decorators.admin.user_admin
@decorators.delete.init
def init(update,context):
    reply_markup = InlineKeyboardMarkup(LANGUAGE_KEYBOARD)
    msg = "Please select your preferred language\n\nPerfavore seleziona la tua lingua di preferenza"
    update.message.reply_text(msg,reply_markup=reply_markup)

@decorators.admin.user_admin
def language_en(update, context):
    chat = update.effective_message.chat_id
    msg = "You have selected the English language for your group"
    query = update.callback_query
    query.answer()
    lang = "EN"
    data = [(lang,chat)]
    GroupRepository().update_language(data)
    query.edit_message_text(msg,parse_mode='HTML')

@decorators.admin.user_admin
def language_it(update, context):
    chat = update.effective_message.chat_id
    msg = "Hai selezionato la lingua italiana per il tuo gruppo"
    query = update.callback_query
    query.answer()
    lang = "IT"
    data = [(lang,chat)]
    GroupRepository().update_language(data)
    query.edit_message_text(msg,parse_mode='HTML')