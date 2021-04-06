from core import decorators
from core.utilities.message import message
from languages.getLang import languages
from core.database.repository.group import GroupRepository

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