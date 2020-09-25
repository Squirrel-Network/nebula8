from core import decorators

@decorators.owner.init
def init(update, context):
    bot = context.bot
    bot.send_message(update.effective_chat.id, "exit")