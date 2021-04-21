#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
import datetime
from core import decorators
from core.database.repository.user import UserRepository
from core.database.repository.group import GroupRepository
from core.utilities.functions import user_reply_object, chat_object
from core.utilities.functions import ban_user_reply
from core.utilities.message import message
from core.handlers.logs import telegram_loggers
from core.utilities.menu import build_menu
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

@decorators.admin.user_admin
@decorators.delete.init
def init(update,context):
    user = user_reply_object(update)
    chat = chat_object(update)
    get_user = UserRepository().getUserByGroup([user.id,chat.id])
    get_group = GroupRepository().getById(chat.id)
    warn_count = get_user['warn_count'] if get_user is not None else 0
    max_warn = get_group['max_warn']
    current_time = datetime.datetime.utcnow().isoformat()
    default_warn = 1

    if warn_count != max_warn:
        if get_user:
            default_warn_count = 0
            username = "@"+user.username
            data = [(username,current_time,user.id)]
            UserRepository().update(data)
            data_mtm = [(user.id, chat.id, default_warn_count)]
            UserRepository().add_into_mtm(data_mtm)
            data_warn = [(user.id,chat.id)]
            UserRepository().updateWarn(data_warn)
            message(update,context,"{} was warned by the group {}".format(username,chat.title))
            log_txt = "#Log {} was warned by the group {}".format(username,chat.title)
            telegram_loggers(update,context,log_txt)
        else:
            username = "@"+user.username
            data = [(user.id,username,current_time,current_time)]
            UserRepository().add(data)
            data_mtm = [(user.id, chat.id, default_warn)]
            UserRepository().add_into_mtm(data_mtm)
            message(update,context,"{} was warned by the group {}".format(username,chat.title))
            log_txt = "#Log {} was warned by the group {}".format(username,chat.title)
            telegram_loggers(update,context,log_txt)
    else:
        ban_user_reply(update,context)
        message(update,context,"User @{} has reached the maximum number\n of warns in the {} group and has been banned".format(user.username,chat.title))



@decorators.admin.user_admin
@decorators.delete.init
def set_warn(update, context):
    bot = context.bot
    chat = update.effective_message.chat_id
    buttons = []
    buttons.append(InlineKeyboardButton('2', callback_data='w2'))
    buttons.append(InlineKeyboardButton('3', callback_data='w3'))
    buttons.append(InlineKeyboardButton('4', callback_data='w4'))
    buttons.append(InlineKeyboardButton('5', callback_data='w5'))
    buttons.append(InlineKeyboardButton('6', callback_data='w6'))
    buttons.append(InlineKeyboardButton('7', callback_data='w7'))
    buttons.append(InlineKeyboardButton('8', callback_data='w8'))
    buttons.append(InlineKeyboardButton('9', callback_data='w9'))
    buttons.append(InlineKeyboardButton('10', callback_data='w10'))
    menu = build_menu(buttons,3)
    bot.send_message(chat,"Warn Settings", reply_markup=InlineKeyboardMarkup(menu),parse_mode='HTML' )

@decorators.admin.user_admin
def update_set_warn(update, context):
    query = update.callback_query
    if query.data.startswith("w"):
        chat_id = query.message.chat_id
        warn_limit = query.data[1:]
        record = GroupRepository.SET_MAX_WARN
        data = [(warn_limit,chat_id)]
        GroupRepository().update_group_settings(record, data)
        text = "You have changed the maximum number\nof warns in this group to <code>{}</code>".format(warn_limit)
        query.edit_message_text(text, parse_mode='HTML')