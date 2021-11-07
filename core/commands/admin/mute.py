#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core import decorators
from core.utilities.message import message
from core.utilities.menu import build_menu
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.utilities.functions import mute_user_reply, mute_user_by_id
from languages.getLang import languages

@decorators.admin.user_admin
@decorators.delete.init
def init(update,context):
    languages(update,context)
    if update.message.reply_to_message:
        user = update.message.reply_to_message.from_user
        buttons = []
        buttons.append(InlineKeyboardButton(languages.mute_button, callback_data='unmute'))
        menu = build_menu(buttons,2)
        msg = languages.mute_msg.format(user.id,user.first_name,user.id)
        update.message.reply_to_message.reply_text(msg, reply_markup=InlineKeyboardMarkup(menu),parse_mode='HTML')
        mute_user_reply(update,context,True)
    else:
        message(update,context,languages.error_response_user_msg)

@decorators.admin.user_admin
def update_mute(update,context):
    query = update.callback_query
    user = query.message.reply_to_message.from_user
    if query.data == 'unmute':
        languages(update,context)
        mute_user_by_id(update,context,user.id,False)
        msg = languages.mute_msg_r.format(user.id,user.first_name,user.id)
        query.edit_message_text(msg, parse_mode='HTML')