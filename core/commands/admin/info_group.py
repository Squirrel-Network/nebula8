from core.database.repository.group import GroupRepository
from languages.getLang import languages
from core.utilities.message import message
from core import decorators

@decorators.admin.user_admin
@decorators.public.init
@decorators.delete.init
def init(update, context):
    languages(update,context)
    chat = update.effective_message.chat_id
    rows = GroupRepository().getById([chat])
    for row in rows:
        message(update,context,languages.group_info.format(
            row['id_group'],
            row['welcome_text'],
            row['rules_text'],
            row['languages']))