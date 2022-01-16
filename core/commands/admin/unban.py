#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core import decorators
from core.utilities.message import message
from telegram.utils.helpers import mention_html
from core.utilities.functions import chat_object, user_reply_object
from core.utilities.functions import reply_member_status_object

@decorators.admin.user_admin
def init(update,context):
    bot = context.bot
    reply = update.message.reply_to_message
    if reply is not None:
        user_status = reply_member_status_object(update,context)
        if user_status.status == 'kicked':
            chat = chat_object(update)
            user = user_reply_object(update)
            message(update,context,"the ban for the user {} <code>[{}]</code> has been removed".format(mention_html(user.id, user.first_name),user.id))
            bot.unban_chat_member(chat.id, user.id)
        else:
            user = user_reply_object(update)
            message(update,context,"the user {} <code>[{}]</code> is not banned".format(mention_html(user.id, user.first_name),user.id))
    else:
        message(update,context,"This command should be used in response to a user!")