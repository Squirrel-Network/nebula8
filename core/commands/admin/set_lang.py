#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core import decorators
from core.database.repository.group import GroupRepository
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.utilities.functions import flag

LANGUAGE_KEYBOARD = [[
    InlineKeyboardButton(flag('gb'), callback_data='language_en'),
    InlineKeyboardButton(flag('it'), callback_data='language_it')
    ]]

record = GroupRepository.SET_LANGUAGE

@decorators.admin.user_admin
def init(update,context):
    bot = context.bot
    chat = update.effective_message.chat_id
    reply_markup = InlineKeyboardMarkup(LANGUAGE_KEYBOARD)
    msg = "Please select your preferred language\n\nPerfavore seleziona la tua lingua di preferenza"
    bot.send_message(chat,msg,reply_markup=reply_markup)

@decorators.admin.user_admin
def language_en(update, context):
    chat = update.effective_message.chat_id
    msg = "You have selected the English language for your group"
    query = update.callback_query
    query.answer()
    lang = "EN"
    data = [(lang,chat)]
    GroupRepository().update_group_settings(record, data)
    query.edit_message_text(msg,parse_mode='HTML')

@decorators.admin.user_admin
def language_it(update, context):
    chat = update.effective_message.chat_id
    msg = "Hai selezionato la lingua italiana per il tuo gruppo"
    query = update.callback_query
    query.answer()
    lang = "IT"
    data = [(lang,chat)]
    GroupRepository().update_group_settings(record, data)
    query.edit_message_text(msg,parse_mode='HTML')