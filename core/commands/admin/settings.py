#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core import decorators
from core.utilities.menu import build_menu
from core.utilities.functions import update_db_settings
from core.utilities.constants import PERM_TRUE, PERM_FALSE, PERM_MEDIA_FALSE, PERM_MEDIA_TRUE
from languages.getLang import languages
from core.commands.admin import set_lang
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.database.repository.group import GroupRepository

def keyboard_settings(update,context,editkeyboard = False):
    bot = context.bot
    chat = update.message.chat_id
    chat_title = update.message.chat.title
    group = GroupRepository().getById(chat)
    list_buttons = []
    list_buttons.append(InlineKeyboardButton('Welcome %s' % ('✅' if group['set_welcome'] == 1 else '❌'), callback_data='setWelcome'))
    list_buttons.append(InlineKeyboardButton('Silence %s' % ('✅' if group['set_silence'] == 1 else '❌'), callback_data='setSilence'))
    list_buttons.append(InlineKeyboardButton('Deny All Entry %s' % ('✅' if group['block_new_member'] == 1 else '❌'), callback_data='setBlockEntry'))
    list_buttons.append(InlineKeyboardButton('No User Photo Entry %s' % ('✅' if group['set_user_profile_picture'] == 1 else '❌'), callback_data='userPhoto'))
    list_buttons.append(InlineKeyboardButton('No Arabic Entry %s' % ('✅' if group['set_arabic_filter'] == 1 else '❌'), callback_data='arabic'))
    list_buttons.append(InlineKeyboardButton('No Russian Entry %s' % ('✅' if group['set_cirillic_filter'] == 1 else '❌'), callback_data='cirillic'))
    list_buttons.append(InlineKeyboardButton('No Chinese Entry %s' % ('✅' if group['set_chinese_filter'] == 1 else '❌'), callback_data='chinese'))
    list_buttons.append(InlineKeyboardButton('No ZooPhile Entry %s' % ('✅' if group['zoophile_filter'] == 1 else '❌'), callback_data='zoophile'))
    list_buttons.append(InlineKeyboardButton('CAS BAN %s' % ('✅' if group['set_cas_ban'] == 1 else '❌'), callback_data='casban'))
    list_buttons.append(InlineKeyboardButton('Languages', callback_data='lang'))
    list_buttons.append(InlineKeyboardButton('Commands', url='https://github.com/Squirrel-Network/nebula8/wiki/Command-List'))
    list_buttons.append(InlineKeyboardButton("Close", callback_data='close'))
    menu = build_menu(list_buttons,2)
    if editkeyboard == False:
        keyboard_menu = bot.send_message(chat,"⚙️ Bot settings\n\n📜 Group Name: <i>{}</i>\n🏷 ChatId: <code>{}</code>".format(chat_title,chat),reply_markup=InlineKeyboardMarkup(menu),parse_mode='HTML')
    if editkeyboard == True:
        keyboard_menu = bot.edit_message_reply_markup(chat,update.message.message_id,reply_markup=InlineKeyboardMarkup(menu))
    return keyboard_menu

@decorators.public.init
@decorators.admin.user_admin
@decorators.bot.check_is_admin
@decorators.delete.init
def init(update,context):
    keyboard_settings(update,context)

@decorators.admin.user_admin
def update_settings(update,context):
    bot = context.bot
    languages(update,context)
    query = update.callback_query
    chat = update.effective_message.chat_id
    group = GroupRepository().getById(chat)
    # Set Welcome
    if query.data == 'setWelcome':
        record = GroupRepository.SET_WELCOME
        row = group['set_welcome']
        if row == 1:
            update_db_settings(update, record, True)
            return keyboard_settings(query,context,True)
        else:
            data_block = [(1,0,chat)]
            update_db_settings(update, record, False)
            GroupRepository().set_block_entry(data_block)
            return keyboard_settings(query,context,True)
    # Set Global Silence
    if query.data == 'setSilence':
        record = GroupRepository.SET_SILENCE
        row = group['set_silence']
        if row == 0:
            update_db_settings(update, record, False)
            bot.set_chat_permissions(update.effective_chat.id, PERM_FALSE)
            return keyboard_settings(query,context,True)
        else:
            update_db_settings(update, record, True)
            bot.set_chat_permissions(update.effective_chat.id, PERM_TRUE)
            return keyboard_settings(query,context,True)
    # Set Block Entry
    if query.data == 'setBlockEntry':
        row = group['block_new_member']
        if row == 0:
            data = [(0,1,chat)]
            GroupRepository().set_block_entry(data)
            return keyboard_settings(query,context,True)
        else:
            data = [(1,0,chat)]
            GroupRepository().set_block_entry(data)
            return keyboard_settings(query,context,True)
    if query.data == 'casban':
        record = GroupRepository.SET_CAS_BAN
        row = group['set_cas_ban']
        if row == 0:
            update_db_settings(update, record, False)
            return keyboard_settings(query,context,True)
        else:
            update_db_settings(update, record, True)
            return keyboard_settings(query,context,True)

    ###################################
    ####  SET WELCOME FILTERS      ####
    ###################################
    # Set Block Arabic Entry
    if query.data == 'arabic':
        record = GroupRepository.SET_ARABIC
        row = group['set_arabic_filter']
        if row == 1:
            update_db_settings(update, record, True)
            return keyboard_settings(query,context,True)
        else:
            update_db_settings(update, record, False)
            return keyboard_settings(query,context,True)
    # Set Block Cirillic Entry
    if query.data == 'cirillic':
        record = GroupRepository.SET_CIRILLIC
        row = group['set_cirillic_filter']
        if row == 1:
            update_db_settings(update, record, True)
            return keyboard_settings(query,context,True)
        else:
            update_db_settings(update, record, False)
            return keyboard_settings(query,context,True)
    if query.data == 'chinese':
        record = GroupRepository.SET_CHINESE
        row = group['set_chinese_filter']
        if row == 1:
            update_db_settings(update, record, True)
            return keyboard_settings(query,context,True)
        else:
            update_db_settings(update, record, False)
            return keyboard_settings(query,context,True)
    if query.data == 'userPhoto':
        record = GroupRepository.SET_USER_PROFILE_PICT
        row = group['set_user_profile_picture']
        if row == 1:
            update_db_settings(update, record, True)
            return keyboard_settings(query,context,True)
        else:
            update_db_settings(update, record, False)
            return keyboard_settings(query,context,True)
    if query.data == 'zoophile':
        record = GroupRepository.ZOOPHILE_FILTER
        row = group['zoophile_filter']
        if row == 1:
            update_db_settings(update, record, True)
            return keyboard_settings(query,context,True)
        else:
            update_db_settings(update, record, False)
            return keyboard_settings(query,context,True)
    ###################################
    ####     SET CHAT LANGUAGE     ####
    ###################################
    if query.data == 'lang':
        set_lang.init(update, context)
        query.edit_message_text("You have closed the settings menu and open languages menu",parse_mode='HTML')

    # Close Menu
    if query.data == 'close':
        query.edit_message_text(languages.close_menu_msg, parse_mode='HTML')