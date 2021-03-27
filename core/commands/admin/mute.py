#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core import decorators
from telegram import ChatPermissions
from core.utilities.message import message
from core.utilities.menu import build_menu
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.utilities.functions import mute_user_reply, mute_user_by_id

@decorators.admin.user_admin
@decorators.delete.init
def init(update,context):
    user = update.message.reply_to_message.from_user
    if update.message.reply_to_message:
        buttons = []
        buttons.append(InlineKeyboardButton('Unmute', callback_data='unmute'))
        menu = build_menu(buttons,2)
        msg = 'You muted the user <a href="tg://user?id={}">{}</a>'.format(user.id,user.id)
        update.message.reply_to_message.reply_text(msg, reply_markup=InlineKeyboardMarkup(menu),parse_mode='HTML')
        mute_user_reply(update,context,True)
    else:
        message(update,context,"You must use this command in response to a user")

@decorators.admin.user_admin
def update_mute(update,context):
    query = update.callback_query
    user_id = query.message.reply_to_message.from_user.id
    if query.data == 'unmute':
        mute_user_by_id(update,context,user_id,False)
        msg = 'You have removed the mute from user <a href="tg://user?id={}">{}</a>'.format(user_id,user_id)
        query.edit_message_text(msg, parse_mode='HTML')