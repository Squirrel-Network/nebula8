#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
import datetime
from core import decorators
from core.utilities.message import message
from core.database.repository.superban import SuperbanRepository
from core.handlers.logs import sys_loggers,telegram_loggers
from core.utilities.strings import Strings
from core.utilities.functions import ban_user_reply,delete_message_reply

@decorators.owner.init
@decorators.delete.init
def init(update,context):
    motivation = update.message.text[2:].strip()
    reply = update.message.reply_to_message
    if reply is not None:
        if motivation != "":
            user_id = reply.from_user.id
            save_date = datetime.datetime.utcnow().isoformat()
            operator_id = update.message.from_user.id
            data = [(user_id,motivation,save_date,operator_id)]
            SuperbanRepository().add(data)
            ban_user_reply(update,context)
            delete_message_reply(update,context)
            logs_text = Strings.SUPERBAN_LOG.format(user_id,motivation,save_date,operator_id)
            message(update,context,"You got super banned <code>{}</code>".format(user_id))
            telegram_loggers(update,context,logs_text)
            formatter = "Superban eseguito da: {}".format(update.message.from_user.id)
            sys_loggers("[SUPERBAN_LOGS]",formatter,False,False,True)
        else:
            message(update,context,"You need to specify a reason for the <b>superban!</b>")
    else:
        message(update,context,"You must use this command in response to a user!")