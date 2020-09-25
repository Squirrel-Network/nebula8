from core.database.repository.group import GroupRepository
from core import decorators

@decorators.admin.user_admin
def init(update, context):
    chat = update.effective_message.chat_id
    rows = GroupRepository().getById([chat])
    for row in rows:
        print(row['id'])
        message = "{}".format(row['id'])
        context.bot.send_message(chat,message)