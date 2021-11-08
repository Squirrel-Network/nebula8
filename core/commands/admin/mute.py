#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

import re
from core import decorators
from core.utilities.message import message
from core.utilities.menu import build_menu
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.utilities.functions import mute_user_reply, mute_user_by_id, mute_user_by_id_time
from languages.getLang import languages
from core.utilities.regex import Regex

@decorators.admin.user_admin
@decorators.delete.init
def init(update,context):
    languages(update,context)
    if update.message.reply_to_message:
        user = update.message.reply_to_message.from_user
        buttons = []
        buttons.append(InlineKeyboardButton(languages.mute_button, callback_data='CMunmute'))
        buttons.append(InlineKeyboardButton('30Sec', callback_data='CM30'))
        buttons.append(InlineKeyboardButton('1 Hour', callback_data='CM3600'))
        buttons.append(InlineKeyboardButton('1 Day', callback_data='CM86400'))
        buttons.append(InlineKeyboardButton('3 Days', callback_data='CM259200'))
        buttons.append(InlineKeyboardButton('7 Days', callback_data='CM604800'))
        buttons.append(InlineKeyboardButton('Forever', callback_data='CMforever'))
        menu = build_menu(buttons,2)
        msg = languages.mute_msg.format(user.id,user.first_name,user.id)
        update.message.reply_to_message.reply_text(msg, reply_markup=InlineKeyboardMarkup(menu),parse_mode='HTML')
        mute_user_reply(update,context,True)
    else:
        text = update.message.text
        input_user_id = text[5:].strip().split(" ", 1)
        user_id = input_user_id[0]
        time_args = input_user_id[1]
        if user_id != "" and time_args != "":
            number = re.search(Regex.HAS_NUMBER, user_id)
            if number is None:
                message(update,context,"Attention you must enter a number not letters!")
            else:
                mute_user_by_id_time(update,context,user_id,True,int(time_args))
                msg = 'You muted the user <a href="tg://user?id={}">{}</a> <code>[{}]</code> for <code>{}</code> seconds'.format(user_id,user_id,user_id,time_args)
                message(update,context,msg)
        else:
            message(update,context,"Attention you have not entered the user id and mute time correctly")

@decorators.admin.user_admin
def update_mute(update,context):
    query = update.callback_query
    user = query.message.reply_to_message.from_user
    if query.data.startswith("CM"):
        txt = query.data[2:]
        if txt == "30":
            mute_user_by_id_time(update,context,user.id,True,int(txt))
            msg = 'You muted the user <a href="tg://user?id={}">{}</a> <code>[{}]</code> for <code>{}</code> seconds'.format(user.id,user.first_name,user.id,txt)
            query.edit_message_text(msg, parse_mode='HTML')
        if txt == "3600":
            mute_user_by_id_time(update,context,user.id,True,int(txt))
            msg = 'You muted the user <a href="tg://user?id={}">{}</a> <code>[{}]</code> for 1 Hour'.format(user.id,user.first_name,user.id)
            query.edit_message_text(msg, parse_mode='HTML')
        if txt == "86400":
            mute_user_by_id_time(update,context,user.id,True,int(txt))
            msg = 'You muted the user <a href="tg://user?id={}">{}</a> <code>[{}]</code> for 1 Day'.format(user.id,user.first_name,user.id)
            query.edit_message_text(msg, parse_mode='HTML')
        if txt == "259200":
            mute_user_by_id_time(update,context,user.id,True,int(txt))
            msg = 'You muted the user <a href="tg://user?id={}">{}</a> <code>[{}]</code> for 3 Day'.format(user.id,user.first_name,user.id)
            query.edit_message_text(msg, parse_mode='HTML')
        if txt == "604800":
            mute_user_by_id_time(update,context,user.id,True,int(txt))
            msg = 'You muted the user <a href="tg://user?id={}">{}</a> <code>[{}]</code> for 7 Day'.format(user.id,user.first_name,user.id)
            query.edit_message_text(msg, parse_mode='HTML')
        if txt == "forever":
            mute_user_by_id(update,context,user.id,True)
            msg = 'You muted the user <a href="tg://user?id={}">{}</a> <code>[{}]</code> forever'.format(user.id,user.first_name,user.id)
            query.edit_message_text(msg, parse_mode='HTML')
        if txt == 'unmute':
            languages(update,context)
            mute_user_by_id(update,context,user.id,False)
            msg = languages.mute_msg_r.format(user.id,user.first_name,user.id)
            query.edit_message_text(msg, parse_mode='HTML')