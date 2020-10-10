import re
from core import decorators
from languages.getLang import languages
from core.database.repository.group import GroupRepository
from core.utilities.message import message
from core.utilities import functions
from core.utilities.functions import delete_message
from telegram.ext.dispatcher import run_async

def welcome_message(update,context,user):
    chat = update.effective_message.chat_id
    rows = GroupRepository().getById([chat])
    for row in rows:
        if row is not None:
            parsed_message = row['welcome_text'].replace('{first_name}',
            update.message.from_user.first_name).replace('{chat_name}',
            update.message.chat.title).replace('{username}',"@"+user.username)
            format_message = "{}".format(parsed_message)
            welcome = update.message.reply_text(format_message,parse_mode='HTML')
            return True
        else:
            return False
    return welcome

def arabic_filter(update,context,user_first_name):
    arabic = re.search("[\u0600-\u06ff]|[\u0750-\u077f]|[\ufb50-\ufbc1]|[\ufbd3-\ufd3f]|[\ufd50-\ufd8f]|[\ufd92-\ufdc7]|[\ufe70-\ufefc]|[\uFDF0-\uFDFD]+",user_first_name)
    if arabic:
        return True
    return arabic

@run_async
def init(update, context):
    for member in update.message.new_chat_members:
        ar_filter = arabic_filter(update,context,member.first_name)
        welcome = welcome_message(update,context,member)
        if ar_filter == True:
            functions.kick_user(update,context)
        if welcome == False:
            update.message.reply_text("DEFAULT",parse_mode='HTML')