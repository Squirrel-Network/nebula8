from core import decorators
from core.utilities.message import message
from core.database.repository.group import GroupRepository

@decorators.admin.user_admin
@decorators.delete.init
def init(update, context):
    record = GroupRepository.SET_RULES_TEXT
    chat = update.effective_chat.id
    msg = update.message.text[9:].strip()
    if msg != "":
        data = [(msg, chat)]
        GroupRepository().update_group_settings(record, data)
        message(update, context, "You have correctly changed the rules of the group!")
    else:
        message(update, context, "The message is empty! The correct format is: <code>/setrules args</code>")