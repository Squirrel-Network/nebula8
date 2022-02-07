#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core.utilities.functions import member_status_object, chat_status_object
from core.utilities.message import message

def init(update,context):
    reply = update.message.reply_to_message
    if reply:
        print("REPLY")
    else:
        print("NO REPLY")
        user_status = member_status_object(update,context)
        chat_status = chat_status_object(update, context)
        if user_status.status == 'creator':
            user = user_status.user
            username = "@"+user.username
            data = [user.id,user.first_name,username,chat_status.id]
            message(update,context,"<i>UNDER CONSTRUCTION {}</i>\n\nSeguici su: https://github.com/Squirrel-Network/nebula8".format(data))
        else:
            msg = "Non sei il proprietario del gruppo non puoi usare questo comando"
            message(update,context,msg)