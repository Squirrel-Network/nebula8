#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core import decorators
from core.utilities.message import message
from core.utilities.functions import chat_object
from core.database.repository.group import GroupRepository

@decorators.admin.user_admin
@decorators.delete.init
def init(update, context):
    chat = chat_object(update)
    msg = update.message.text[7:]
    reply = update.message.reply_to_message
    if reply:
        custom_question = str(reply.text)
        if custom_question == '/test':
            message(update, context, 'This command is reserved for the bot!')
        else:
            custom_answer = str(msg).lower()
            data = [(chat.id,custom_question,custom_answer)]
            GroupRepository().insert_custom_handler(data)
            message(update,context,"<b>Custom handler setted!</b>\n\nQuestion: <code>{}</code>\nAnswer: <code>{}</code>".format(custom_question,custom_answer))
    else:
        message(update,context,"You must reply to a message to use this command!")