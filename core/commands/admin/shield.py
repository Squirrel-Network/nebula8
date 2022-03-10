#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core import decorators
from languages.getLang import languages
from core.utilities.functions import chat_object,update_db_settings
from core.database.repository.group import GroupRepository
from core.utilities.constants import PERM_FALSE, PERM_TRUE
from core.utilities.menu import build_menu
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.handlers.logs import telegram_loggers

@decorators.admin.user_admin
@decorators.delete.init
def init(update, context):
    bot = context.bot
    chat = chat_object(update)
    languages(update,context)
    record_arabic = GroupRepository.SET_ARABIC
    record_chinese = GroupRepository.SET_CHINESE
    record_cirillic = GroupRepository.SET_CIRILLIC
    record_no_user_photo = GroupRepository.SET_USER_PROFILE_PICT
    record_silence = GroupRepository.SET_SILENCE
    record_block_channel = GroupRepository.SENDER_CHAT_BLOCK
    record_zoophile = GroupRepository.ZOOPHILE_FILTER


    data = [(0,1,chat.id)]
    GroupRepository().set_block_entry(data)
    update_db_settings(update, record_arabic, False)
    update_db_settings(update, record_chinese, False)
    update_db_settings(update, record_cirillic, False)
    update_db_settings(update, record_no_user_photo, False)
    update_db_settings(update, record_silence, False)
    update_db_settings(update, record_block_channel, False)
    update_db_settings(update, record_zoophile, False)
    buttons = []
    buttons.append(InlineKeyboardButton('❌ Remove Shield', callback_data='removeShield'))
    menu = build_menu(buttons,1)

    bot.set_chat_permissions(update.effective_chat.id, PERM_FALSE)
    bot.send_message(chat.id,languages.shield_on,reply_markup=InlineKeyboardMarkup(menu),parse_mode='HTML')
    logs_text = '🛡Shield Activated in {} <code>[{}]</code>'.format(chat.title,chat.id)
    telegram_loggers(update,context,logs_text)

@decorators.admin.user_admin
def update_shield(update,context):
    bot = context.bot
    query = update.callback_query
    if query.data == 'removeShield':
        chat = update.effective_message.chat_id
        chat_title = update.effective_message.chat.title
        record_arabic = GroupRepository.SET_ARABIC
        record_chinese = GroupRepository.SET_CHINESE
        record_cirillic = GroupRepository.SET_CIRILLIC
        record_no_user_photo = GroupRepository.SET_USER_PROFILE_PICT
        record_silence = GroupRepository.SET_SILENCE
        record_block_channel = GroupRepository.SENDER_CHAT_BLOCK
        record_zoophile = GroupRepository.ZOOPHILE_FILTER


        data = [(1,0,chat)]
        GroupRepository().set_block_entry(data)
        update_db_settings(update, record_arabic, True)
        update_db_settings(update, record_chinese, True)
        update_db_settings(update, record_cirillic, True)
        update_db_settings(update, record_no_user_photo, True)
        update_db_settings(update, record_silence, True)
        update_db_settings(update, record_block_channel, True)
        update_db_settings(update, record_zoophile, True)
        bot.set_chat_permissions(update.effective_chat.id, PERM_TRUE)
        msg = '✅ Shield removed!'
        query.edit_message_text(msg, parse_mode='HTML')
        logs_text = '🛡Shield Deactivated in {} <code>[{}]</code>'.format(chat_title,chat)
        telegram_loggers(update,context,logs_text)