#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

# Copyright SquirrelNetwork
from config import Config
from core import decorators
from core.utilities.message import message
from core.handlers.logs import sys_loggers
from core.utilities.functions import chat_object
from core.utilities.message import ApiGroupRemove
#from core.database.repository.group import GroupRepository

#TODO NEED FIX DELETE GROUP IN DATABASE

@decorators.owner.init
def init(update, context):
    bot = context.bot
    chat = chat_object(update)
    #GroupRepository.remove(chat.id)
    bot.leaveChat(update.message.chat_id)
    message(update, context, "#Log the bot has left the chat <code>{}</code>\nby operator <code>{}</code>".format(chat.id,update.message.from_user.id), 'HTML', 'messageid', Config.DEFAULT_LOG_CHANNEL, None)
    formatter = "Il bot è uscito dalla chat {} e il comando è stato eseguito da: {}".format(chat.id,update.message.from_user.id)
    sys_loggers("[BOT_EXIT_LOGS]",formatter,False,False,True)

@decorators.owner.init
def remote_exit(update,context):
    try:
        text = update.message.text
        input_user_id = text[6:].strip().split(" ", 1)
        chatid = input_user_id[0]
        message(update,context,"The bot remotely exited the following group: <code>{}</code>".format(chatid))
        time.sleep(1)
        ApiGroupRemove(chatid)
    except Exception as e:
        print(e)