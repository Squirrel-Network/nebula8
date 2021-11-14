#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core import decorators
from core.utilities.menu import build_menu
from languages.getLang import languages
from core.database.repository.group import GroupRepository
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

@decorators.public.init
@decorators.delete.init
def init(update, context):
    bot = context.bot
    languages(update,context)
    chat = update.effective_message.chat_id
    chat_title = update.message.chat.title
    list_buttons = []
    list_buttons.append(InlineKeyboardButton(languages.rules_button, callback_data='openRules'))
    menu = build_menu(list_buttons,1)
    bot.send_message(chat,languages.rules_main.format(chat_title,chat),reply_markup=InlineKeyboardMarkup(menu),parse_mode='HTML')


def update_rules(update,context):
    query = update.callback_query
    if query.data == 'openRules':
        languages(update,context)
        chat = update.effective_message.chat_id
        row = GroupRepository().getById([chat])
        query.edit_message_text(languages.rules.format(row['rules_text']),parse_mode='HTML')