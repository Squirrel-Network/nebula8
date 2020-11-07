import re
from config import Config
from core import decorators
from languages.getLang import languages
from core.database.repository.group import GroupRepository
from core.database.repository.user import UserRepository
from core.database.repository.superban import SuperbanRepository
from core.utilities.message import message, reply_message
from core.utilities import functions
from core.utilities.functions import delete_message
from core.utilities.regex import Regex
from telegram.ext.dispatcher import run_async
from core.utilities.functions import kick_user, ban_user
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

LANGUAGE_KEYBOARD = [[
    InlineKeyboardButton("EN", callback_data='select_language_en'),
    InlineKeyboardButton("IT", callback_data='select_language_it')
    ]]

def has_arabic_character(string):
    arabic = re.search(Regex.HAS_ARABIC, string.first_name)
    return not not arabic

def save_user(member):
    # Save the user in the database and check that it exists if it exists and has changed nickname overwrite
    user = UserRepository().getById(member.id)
    if user:
        username = "@"+member.username
        data = [(username,member.id)]
        UserRepository().update(data)
    else:
        username = "@"+member.username
        data = [(member.id,username)]
        UserRepository().add(data)

def save_group(update):
    chat = update.effective_message.chat_id
    group = GroupRepository().getById(chat)
    if group:
        print('update')
        #data = [(chat,chat)]
        #GroupRepository().update(data)
    else:
        default_lang = Config.DEFAULT_LANGUAGE
        data = [(chat,"","",1,default_lang)]
        GroupRepository().add(data)

def is_in_blacklist(uid):
    return not not SuperbanRepository().getById(uid)

def welcome_user(update, context, member):
    # Check that the welcome exists on the database if there is no Default Welcome
    chat = update.effective_message.chat_id

    group = GroupRepository().getById(chat)
    if group is not None:
        parsed_message = group['welcome_text'].replace(
            '{first_name}',
            update.message.from_user.first_name).replace('{chat_name}',
            update.message.chat.title).replace('{username}',
            "@"+member.username
        )
        format_message = "{}".format(parsed_message)
        reply_message(update, context, format_message)
    else:
        chat_title = update.effective_chat.title
        default_welcome = Config.DEFAULT_WELCOME.format("@"+member.username,chat_title)
        reply_message(update, context,default_welcome)


def welcome_bot(update, context):
    reply_markup = InlineKeyboardMarkup(LANGUAGE_KEYBOARD)
    msg = "Please select your preferred language\n\nPerfavore seleziona la tua lingua di preferenza"
    save_group(update)
    update.message.reply_text(msg,reply_markup=reply_markup)

@decorators.admin.user_admin
def select_language_en(update, context):
    chat = update.effective_message.chat_id
    msg = "You have selected the English language for your group"
    query = update.callback_query
    query.answer()
    lang = "EN"
    data = [(lang,chat)]
    GroupRepository().update_language(data)
    query.edit_message_text(msg,parse_mode='HTML')

@decorators.admin.user_admin
def select_language_it(update, context):
    chat = update.effective_message.chat_id
    msg = "Hai selezionato la lingua italiana per il tuo gruppo"
    query = update.callback_query
    query.answer()
    lang = "IT"
    data = [(lang,chat)]
    GroupRepository().update_language(data)
    query.edit_message_text(msg,parse_mode='HTML')

@run_async
def init(update, context):
    for member in update.message.new_chat_members:

        if member.is_bot:
            welcome_bot(update, context)

        else:
            save_user(member)

            if member.username is None:
                kick_user(update, context)

            # TODO: add flag blacklist active
            elif is_in_blacklist(member.id) or has_arabic_character(member):
                ban_user(update, context)

            else:
                welcome_user(update, context, member)