#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from functools import wraps
from core.utilities.functions import bot_object

def check_is_admin(func):
    @wraps(func)
    def wrapped(update, context):
        bot = bot_object(update, context)
        chat = update.effective_message.chat_id
        get_bot = bot.getChatMember(chat,bot.id)
        if get_bot.status == 'administrator':
            print("is_admin")
        else:
            update.effective_message.reply_text("I'm not admin!")
            return False
        return func(update, context)
    return wrapped

def check_can_delete(func):
    @wraps(func)
    def wrapped(update, context):
        bot = bot_object(update, context)
        chat = update.effective_message.chat_id
        get_bot = bot.getChatMember(chat,bot.id)
        perm_delete = get_bot.can_delete_messages
        print(perm_delete)
        if perm_delete is not False:
            print("can_delete")
        else:
            update.effective_message.reply_text("I can't delete messages here!\nMake sure I'm admin and can delete other user's messages.")
            return False
        return func(update, context)
    return wrapped