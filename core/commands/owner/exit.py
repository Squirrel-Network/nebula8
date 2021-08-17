#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from config import Config
from core import decorators
from core.utilities.message import messageWithId
from core.handlers.logs import sys_loggers
from core.utilities.functions import chat_object

@decorators.owner.init
def init(update, context):
    bot = context.bot
    chat = chat_object(update)
    bot.leaveChat(update.message.chat_id)
    messageWithId(update,context,Config.DEFAULT_LOG_CHANNEL,"#Log the bot has left the chat <code>{}</code>\nby operator <code>{}</code>".format(chat.id,update.message.from_user.id))
    formatter = "Il bot è uscito dalla chat {} e il comando è stato eseguito da: {}".format(chat.id,update.message.from_user.id)
    sys_loggers("[BOT_EXIT_LOGS]",formatter,False,False,True)