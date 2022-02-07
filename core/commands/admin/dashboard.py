#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core.utilities.functions import member_status_object, chat_status_object

def init(update,context):
    reply = update.message.reply_to_message
    if reply:
        print("REPLY")
    else:
        print("NO REPLY")
        user_status = member_status_object(update,context)
        chat_status = chat_status_object(update, context)
        if user_status.status == 'creator':
            print(user_status)
            print(chat_status)
            print("CREATOR OK")
        else:
            print("NO CREATOR")
        
