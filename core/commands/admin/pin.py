#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core import decorators
from core.utilities.message import message

@decorators.admin.user_admin
@decorators.delete.init
def pin(update,context):
    bot = context.bot
    reply = update.message.reply_to_message
    if reply:
        msg = str(reply.text).strip()
        if reply.photo:
            caption = update.message.reply_to_message.caption
            update.message.reply_to_message.reply_photo(photo=reply.photo[-1].file_id, caption=caption)
            bot.pin_chat_message(update.message.chat_id, update.message.message_id+1,disable_notification=True)
        else:
            message(update,context,msg)
            bot.pin_chat_message(update.message.chat_id, update.message.message_id+1,disable_notification=True)
    else:
        msg = update.message.text[4:].strip()
        message(update,context,msg)
        bot.pin_chat_message(update.message.chat_id, update.message.message_id+1,disable_notification=True)

@decorators.admin.user_admin
@decorators.delete.init
def unpin_all(update, context):
    bot = context.bot
    bot.unpin_all_chat_messages(chat_id=update.effective_chat.id)
    message(update,context,"All messages have been <b>Unpinned!</b>")