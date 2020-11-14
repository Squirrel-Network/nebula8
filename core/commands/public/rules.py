from core.database.repository.group import GroupRepository
from languages.getLang import languages
from core.utilities.message import message
from core import decorators

@decorators.public.init
@decorators.delete.init
def init(update, context):
    languages(update,context)
    chat = update.effective_message.chat_id
    row = GroupRepository().getById([chat])
    message(update,context,languages.rules.format(row['rules_text']))