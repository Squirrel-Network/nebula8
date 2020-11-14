from core import decorators
from core.handlers.logs import sys_loggers,telegram_loggers
from core.utilities.message import message
from core.utilities.strings import Strings
from core.utilities.functions import bot_object
from languages.getLang import languages
from core.utilities.functions import ban_user_reply,delete_message_reply

#TODO Da completare o rivedere
@decorators.admin.user_admin
def init(update, context):
    languages(update,context)
    bot = bot_object(update,context)
    chat = update.effective_chat
    reply = update.message.reply_to_message
    if reply is not None:
        if reply.from_user.id == bot.id:
            text = "Non posso bannarmi da sola!"
            message(update,context,text)
        else:
            ban_text = languages.ban_message.format(
            user=reply.from_user.username or reply.from_user.first_name,
            userid=reply.from_user.id,
            chat=chat.title,
            motivation= "TEST NEBULA 8.0.0"
            )
            logs_text = Strings.BAN_LOG.format(
                username=reply.from_user.username or reply.from_user.first_name,
                id=reply.from_user.id,
                chat=chat.title,
                 motivation="TEST NEBULA 8.0.0"
            )
            delete_message_reply(update,context)
            ban_user_reply(update,context)
            message(update,context,ban_text)
            telegram_loggers(update,context,logs_text)
            formatter = "Ban eseguito da: {} nella chat {}".format(
                update.message.from_user.id,
                chat.title)
            sys_loggers("[BAN_LOGS]",formatter,False,True)
    elif reply is None:
        banana = "You must use this command in response to a user!"
        message(update,context,banana)