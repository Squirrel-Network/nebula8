#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
# Credits https://github.com/PaulSonOfLars/tgbot/
import logging
from core import decorators
from config import Config
from telegram.error import BadRequest, Unauthorized
from core.utilities.message import messageWithId, message
from core.database.repository.group import GroupRepository

def sys_loggers(name="",message="",debugs = False,info = False,warning = False,errors = False, critical = False):
    logger = logging.getLogger(name)
    logger.setLevel((logging.INFO, logging.DEBUG)[Config.DEBUG])
    fh = logging.FileHandler('debug.log')
    fh.setLevel(logging.INFO)
    logger.addHandler(fh)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    if debugs == True:
        logger.debug(message)
    elif info == True:
        logger.info(message)
    elif warning == True:
        logger.warning(message)
    elif errors == True:
        logger.error(message)
    elif critical == True:
        logger.critical(message)

def telegram_loggers(update,context,msg = ""):
    chat = update.effective_message.chat_id
    row = GroupRepository().getById([chat])
    id_channel = Config.DEFAULT_LOG_CHANNEL
    if row:
        get_log_channel = row['log_channel']
        send = messageWithId(update,context,get_log_channel,msg)
    else:
        send = messageWithId(update,context,id_channel,msg)
    return send

def staff_loggers(update,context,msg = ""):
    id_staff_group = Config.DEFAULT_STAFF_GROUP
    send = messageWithId(update,context,id_staff_group,msg)
    return send


def set_log_channel(update,context):
        msg = update.effective_message
        chat = update.effective_chat
        if chat.type == 'channel' and str(update.effective_message.text).lower().startswith("/setlog"):
            msg.reply_text("Now, forward the /setlog to the group you want to tie this channel to!")

        elif msg.forward_from_chat:
            data = [(msg.forward_from_chat.id, chat.id)]
            GroupRepository().update_log_channel(data)
            try:
                msg.delete()
            except BadRequest as excp:
                if excp.message == "Message to delete not found":
                    pass
                else:
                    message(update,context,"Error deleting message in log channel. Should work anyway though.")

            try:
                messageWithId(update,context,msg.forward_from_chat.id,"This channel has been set as the log channel for {}.".format(chat.title or chat.first_name))
            except Unauthorized as excp:
                if excp.message == "Forbidden: bot is not a member of the channel chat":
                    message(update,context, "Successfully set log channel!")
                else:
                    print("ERROR in setting the log channel.")

            message(update,context, "Successfully set log channel!")

        else:
            if str(update.effective_message.text).lower().startswith("/setlog"):
                msg.reply_text("The steps to set a log channel are:\n"
                               " - add bot to the desired channel\n"
                               " - send /setlog to the channel\n"
                               " - forward the /setlog to the group\n")