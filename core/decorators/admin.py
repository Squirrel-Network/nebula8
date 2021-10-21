#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from functools import wraps
from core.decorators.owner import OWNER_LIST

TITLES = ['creator', 'administrator']

def user_admin(func):
    @wraps(func)
    def wrapped(update, context):
        user_id = update.effective_user
        try:
            stat = context.bot.get_chat_member(update.message.chat_id, update.effective_user['id'])['status']
        except:
            stat = context.bot.get_chat_member(update.callback_query.message.chat_id, update.callback_query.from_user['id'])['status']
        if (user_id['id'] not in OWNER_LIST) and (stat not in TITLES):
            print("Unauthorized access denied for {}.".format(user_id['id']))
            return
        return func(update, context)
    return wrapped