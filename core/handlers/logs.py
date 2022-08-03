#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
# Credits https://github.com/PaulSonOfLars/tgbot/
import logging
from config import Config
from telegram.error import BadRequest, Unauthorized
from core.utilities.message import message
from core.database.repository.group import GroupRepository

SET_CHANNEL_DEBUG = True

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

"""
This function makes a logger on the telegram channel
set if it is not set it is sent to the default channel
"""
def telegram_loggers(update,context,msg = ""):
    chat = update.effective_message.chat_id
    row = GroupRepository().getById([chat])
    id_channel = Config.DEFAULT_LOG_CHANNEL
    if row:
        get_log_channel = row['log_channel']
        send = message(update, context, msg, 'HTML', 'messageid', get_log_channel, None)
    else:
        send = message(update, context, msg, 'HTML', 'messageid', id_channel, None)
    return send

def staff_loggers(update,context,msg = ""):
    id_staff_group = Config.DEFAULT_STAFF_GROUP
    send = message(update, context, msg, 'HTML', 'messageid', id_staff_group, None)
    return send

def debug_channel(update,context,msg = ""):
    id_debug_channel = -1001540824311
    if SET_CHANNEL_DEBUG == True:
        send = message(update, context, msg, 'HTML', 'messageid', id_debug_channel, None)
    else:
        return
    return send

def set_log_channel(update,context):
        msg = update.effective_message
        chat = update.effective_chat
        user = update.effective_user
        record = GroupRepository.SET_LOG_CHANNEL
        if user is not None:
            member = chat.get_member(user.id)
        if chat.type == 'channel' and str(update.effective_message.text).lower().startswith("/setlog"):
            msg.reply_text("Now, forward the /setlog to the group you want to tie this channel to!")

        elif msg.forward_from_chat and msg.text == '/setlog' and member.status == 'creator':
            data = [(msg.forward_from_chat.id, chat.id)]
            GroupRepository().update_group_settings(record, data)
            try:
                msg.delete()
            except BadRequest as excp:
                if excp.message == "Message to delete not found":
                    pass
                else:
                    message(update,context,"Error deleting message in log channel. Should work anyway though.")

            try:
                msg = "This channel has been set as the log channel for {}.".format(chat.title or chat.first_name)
                message(update, context, msg, 'HTML', 'messageid', msg.forward_from_chat.id, None)
            except Unauthorized as excp:
                if excp.message == "Forbidden: bot is not a member of the channel chat":
                    message(update,context, "Successfully set log channel!")
                else:
                    message(update,context,"ERROR in setting the log channel.")

            message(update,context, "Successfully set log channel!")

        else:
            if str(update.effective_message.text).lower().startswith("/setlog"):
                msg.reply_text("The steps to set a log channel are:\n"
                               " - add bot to the desired channel\n"
                               " - send /setlog to the channel\n"
                               " - forward the /setlog to the group\n"
                               " - You need to be a creator of the group")