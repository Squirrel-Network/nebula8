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
            #file_id = reply.photo[2].file_id
            #get_file = bot.get_file(file_id)
            #url = get_file['file_path']
            #print(url)
            #bot.sendPhoto(chat_id=update.effective_chat.id, photo=url, caption="sddsdsdsds", parse_mode='HTML')
            #message(update, context, "caption", 'HTML', 'photo', None, url)
            #bot.pin_chat_message(update.message.chat_id, update.message.message_id+1,disable_notification=True)
            message(update,context,"You can't pin an image")
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