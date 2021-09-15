from core import decorators
from core.utilities.message import message
from languages.getLang import languages
from core.database.repository.group import GroupRepository

@decorators.admin.user_admin
@decorators.delete.init
def init(update, context):
    record = GroupRepository.SET_RULES_TEXT
    chat = update.effective_chat.id
    msg = update.message.text[9:].strip()
    languages(update,context)
    if msg != "":
        data = [(msg, chat)]
        GroupRepository().update_group_settings(record, data)
        message(update, context, languages.rules_msg)
    else:
        message(update, context, languages.rules_error_msg)