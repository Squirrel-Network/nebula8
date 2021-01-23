from core.utilities.message import message
from core.database.repository.group import GroupRepository

def init(update, context):
    if update.message.migrate_from_chat_id is not None:
        old_chat_id = update.message.migrate_from_chat_id
        new_chat_id = update.message.chat.id
        data = [(new_chat_id, old_chat_id)]
        GroupRepository().update(data)
        message(update,context,"<b>#Automatic handler:</b>\nThe chat has been migrated to <b>supergroup</b> the bot has made the modification on the database.\n<i>It is necessary to put the bot admin</i>")