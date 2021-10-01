#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
import datetime
from core.utilities.message import message
from core.handlers.welcome import welcome_bot
from core.handlers.logs import telegram_loggers
from core.database.repository.group import GroupRepository
from core.utilities.functions import chat_object

def check_status(update, context):
    chat_title = update.effective_chat.title
    chat_id = update.effective_chat.id
    record_title = GroupRepository.SET_GROUP_NAME

    if update.effective_message.migrate_from_chat_id is not None:
        old_chat_id = update.message.migrate_from_chat_id
        new_chat_id = update.message.chat.id
        data = [(new_chat_id, old_chat_id)]
        GroupRepository().update(data)
        message(update,context,"<b>#Automatic handler:</b>\nThe chat has been migrated to <b>supergroup</b> the bot has made the modification on the database.\n<i>It is necessary to put the bot admin</i>")

    if update.effective_message.group_chat_created == True or update.effective_message.supergroup_chat_created == True:
        welcome_bot(update,context)
        l_txt = "#Log <b>Bot added to group</b> {}\nId: <code>{}</code>".format(chat_title,chat_id)
        telegram_loggers(update,context,l_txt)

    if update.effective_message.new_chat_title:
        data = [(chat_title,chat_id)]
        GroupRepository().update_group_settings(record_title,data)

def check_updates(update):
      chat = chat_object(update)
      date = datetime.datetime.utcnow().isoformat()
      if chat.type == "supergroup" or chat.type == "group":
          data = [(update.update_id, chat.id, date)]
          GroupRepository().insert_updates(data)