def init(update, context):
    old_chat_id = update.message.migrate_from_chat_id
    new_chat_id = update.message.chat.id
    print(old_chat_id)
    print(new_chat_id)