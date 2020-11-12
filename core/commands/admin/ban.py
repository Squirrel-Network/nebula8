from core import decorators
from core.handlers.logs import sys_loggers,telegram_loggers
from core.utilities.message import message

@decorators.admin.user_admin
def init(update, context):
    text = "Ban"
    message(update,context,text)
    formatter = "Eseguito Ban da: {}".format(update.message.from_user.id)
    telegram_loggers(update,context,"TEST")
    sys_loggers("[BAN_LOGS]",formatter,False,True)