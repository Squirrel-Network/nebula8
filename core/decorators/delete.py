from functools import wraps

def init(func):
    @wraps(func)
    def wrapped(update, context):
        bot = context.bot
        if update.message.text is not None:
            if update.message.text.startswith("/"):
                bot.delete_message(update.effective_message.chat_id, update.message.message_id)
            else:
                print("AAA")
        return func(update, context)
    return wrapped