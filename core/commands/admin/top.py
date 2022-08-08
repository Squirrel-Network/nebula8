#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

import string
from core.database.repository.group import GroupRepository
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.utilities.functions import chat_object
from core.utilities.message import message
from core.utilities.menu import build_menu
from core import decorators

@decorators.admin.user_admin
@decorators.bot.check_is_admin
@decorators.public.init
@decorators.bot.check_can_delete
@decorators.delete.init
def init(update, context):
    bot = context.bot
    chat = update.effective_message.chat_id
    list_buttons = []
    list_buttons.append(InlineKeyboardButton('Active', callback_data='useractive'))
    list_buttons.append(InlineKeyboardButton('Inactive', callback_data='userinactive'))
    menu = build_menu(list_buttons,1)
    bot.send_message(chat,'Please select an option',reply_markup=InlineKeyboardMarkup(menu),parse_mode='HTML')

@decorators.admin.user_admin
def update_top(update,context):
    query = update.callback_query
    if query.data == 'useractive':
        chat = update.effective_message.chat_id
        topUsers = GroupRepository().getTopActiveUsers(chat)
        string = ""
        for row in topUsers:
            string += "▪️ {} <code>[{}]</code>\n".format(row['tg_username'],row['counter'])
        query.edit_message_text('Top 10 Active Users Until 30 Days\n\n{}'.format(string),parse_mode='HTML')
    if query.data == 'userinactive':
        chat = update.effective_message.chat_id
        topUsers = GroupRepository().getTopInactiveUsers(chat)
        string = ""
        for row in topUsers:
            string += "▪️ {} <code>[{}]</code>\n".format(row['tg_username'],row['counter'])
        query.edit_message_text('Top 10 Inactive Users Until 30 Days\n\n{}'.format(string),parse_mode='HTML')