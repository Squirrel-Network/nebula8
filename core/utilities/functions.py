import time

def kick_user(update,context):
    bot = context.bot
    chat = update.effective_chat.id
    user = update.message.from_user.id
    kick = bot.kick_chat_member(chat,user)
    return kick

def kick_temporary_user(update,context):
    bot = context.bot
    chat = update.effective_chat.id
    kick_temp = bot.kick_chat_member(chat, update.message.from_user.id,until_date=int(time.time()+30))
    return kick_temp

def delete_message(update, context):
    bot = context.bot
    chat = update.effective_chat.id
    id_message = update.message.message_id
    delete = bot.delete_message(chat,id_message)
    return delete