#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
import datetime
from core import decorators
from core.database.repository.user import UserRepository
from core.database.repository.group import GroupRepository
from core.utilities.functions import user_reply_object, chat_object, ban_user_reply, ban_user_by_id
from core.utilities.message import message
from core.handlers.logs import telegram_loggers
from core.utilities.menu import build_menu
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from languages.getLang import languages

@decorators.admin.user_admin
@decorators.delete.init
def init(update,context):
    chat = chat_object(update)
    get_group = GroupRepository().getById(chat.id)
    max_warn = get_group['max_warn']
    current_time = datetime.datetime.utcnow().isoformat()
    default_warn = 1
    languages(update,context)
    if update.message.reply_to_message:
        user = user_reply_object(update)
        get_user = UserRepository().getUserByGroup([user.id,chat.id])
        warn_count = get_user['warn_count'] if get_user is not None else 0
        if warn_count != max_warn:
            buttons = []
            buttons.append(InlineKeyboardButton('➖ 1', callback_data='downWarn'))
            buttons.append(InlineKeyboardButton('➕ 1', callback_data='upWarn'))
            buttons.append(InlineKeyboardButton(languages.button_remove, callback_data='removeWarn'))
            buttons.append(InlineKeyboardButton('Close', callback_data='closeMenu'))
            menu = build_menu(buttons,3)
            if get_user:
                default_warn_count = 0
                username = "@"+user.username
                data = [(username,current_time,user.id)]
                UserRepository().update(data)
                data_mtm = [(user.id, chat.id, default_warn_count)]
                UserRepository().add_into_mtm(data_mtm)
                data_warn = [(user.id,chat.id)]
                UserRepository().updateWarn(data_warn)
                msg = languages.warn_user.format(username,chat.title,chat.id)
                update.message.reply_to_message.reply_text(msg, reply_markup=InlineKeyboardMarkup(menu),parse_mode='HTML')
                log_txt = "‼️ #Log {} was warned\nin the group: {} <code>[{}]</code>".format(username,chat.title,chat.id)
                telegram_loggers(update,context,log_txt)
            else:
                username = "@"+user.username
                data = [(user.id,username,current_time,current_time)]
                UserRepository().add(data)
                data_mtm = [(user.id, chat.id, default_warn)]
                UserRepository().add_into_mtm(data_mtm)
                message(update,context,languages.warn_user.format(username,chat.title,chat.id))
                log_txt = "‼️ #Log {} was warned\nin the group: {} <code>[{}]</code>".format(username,chat.title,chat.id)
                telegram_loggers(update,context,log_txt)
        else:
            ban_user_reply(update,context)
            buttons = []
            buttons.append(InlineKeyboardButton('Remove', callback_data='removeWarn'))
            menu = build_menu(buttons,2)
            msg = languages.warn_user_max.format(user.username,chat.title)
            update.message.reply_to_message.reply_text(msg, reply_markup=InlineKeyboardMarkup(menu),parse_mode='HTML')
    else:
        message(update,context,languages.error_response_user_msg)



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
    bot.send_message(chat,"⚙️ Warn Settings", reply_markup=InlineKeyboardMarkup(menu),parse_mode='HTML' )

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

@decorators.admin.user_admin
def update_warn(update,context):
    query = update.callback_query
    user_id = query.message.reply_to_message.from_user.id
    chat_id = query.message.reply_to_message.chat_id
    get_user = UserRepository().getUserByGroup([user_id,chat_id])
    get_group = GroupRepository().getById(chat_id)
    max_warn = get_group['max_warn']
    warn_count = get_user['warn_count'] if get_user is not None else 0
    if query.data == 'upWarn':
        if warn_count != max_warn:
            data_warn = [(user_id,chat_id)]
            UserRepository().updateWarn(data_warn)
            msg = 'You Upwarned: <a href="tg://user?id={}">{}</a>'.format(user_id,user_id)
            query.edit_message_text(msg, parse_mode='HTML')
        else:
            ban_user_by_id(update,context,user_id)
            msg = "The user has been banned because it has reached the maximum number of warns"
            query.edit_message_text(msg, parse_mode='HTML')
    if query.data == 'downWarn':
        if warn_count != 0:
            data_warn = [(user_id,chat_id)]
            UserRepository().downWarn(data_warn)
            msg = 'You Downwarned: <a href="tg://user?id={}">{}</a>'.format(user_id,user_id)
            query.edit_message_text(msg, parse_mode='HTML')
        else:
            msg = "The user cannot be downwarned anymore!"
            query.edit_message_text(msg, parse_mode='HTML')
    if query.data == 'removeWarn':
        data_warn = [(user_id,chat_id)]
        UserRepository().removeWarn(data_warn)
        msg = 'You have removed the Warns from user: <a href="tg://user?id={}">{}</a>'.format(user_id,user_id)
        query.edit_message_text(msg, parse_mode='HTML')