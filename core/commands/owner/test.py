#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core import decorators

@decorators.owner.init
def init(update,context):
    bot = context.bot
    chat = update.effective_chat.id
    thread_id = update.effective_message.message_thread_id
    text = "Test"
    bot.send_message(chat, text, parse_mode='HTML',message_thread_id=thread_id)