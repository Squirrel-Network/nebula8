from core.database.repository.group_language import GroupLanguageRepository
from core import decorators

@decorators.owner.init
def init(update, context):
    chat = update.effective_message.chat_id
    row = GroupLanguageRepository().getById([chat])
    print(row['languages'])
    message = "{}".format(row['languages'])
    context.bot.send_message(chat,message)