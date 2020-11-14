import datetime
from core import decorators
from core.utilities.message import message
from core.database.repository.superban import SuperbanRepository
from core.handlers.logs import sys_loggers,telegram_loggers
from core.utilities.strings import Strings

@decorators.owner.init
def init(update,context):
    motivation = update.message.text[2:]
    reply = update.message.reply_to_message
    if reply is not None:
        if motivation != "":
            user_id = reply.from_user.id
            save_date = datetime.datetime.utcnow().isoformat()
            operator_id = update.message.from_user.id
            data = [(user_id,motivation,save_date,operator_id)]
            SuperbanRepository().add(data)
            logs_text = Strings.SUPERBAN_LOG.format(user_id,motivation,save_date,operator_id)
            telegram_loggers(update,context,logs_text)
        else:
            message(update,context,"You need to specify a reason for the <b>superban!</b>")
    else:
        message(update,context,"You must use this command in response to a user!")
    formatter = "Superban eseguito da: {}".format(update.message.from_user.id)
    sys_loggers("[SUPERBAN_LOGS]",formatter,False,False,True)