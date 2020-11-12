from core import decorators

@decorators.owner.init
def init(update, context):
    bot = context.bot
    bot.leaveChat(update.message.chat_id)