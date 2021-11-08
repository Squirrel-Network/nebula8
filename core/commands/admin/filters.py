#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core import decorators
from core.utilities.menu import build_menu
from core.utilities.functions import update_db_settings
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.database.repository.group import GroupRepository

def keyboard_filters(update,context,editkeyboard = False):
    bot = context.bot
    chat = update.message.chat_id
    chat_title = update.message.chat.title
    group = GroupRepository().getById(chat)
    list_buttons = []
    list_buttons.append(InlineKeyboardButton('❇️ Activate All', callback_data='ffseall'))
    list_buttons.append(InlineKeyboardButton('⛔️ Deactivate All', callback_data='ffdeall'))
    list_buttons.append(InlineKeyboardButton('Exe Filters %s' % ('✅' if group['exe_filter'] == 1 else '❌'), callback_data='ffexe_filters'))
    list_buttons.append(InlineKeyboardButton('GIF Filters %s' % ('✅' if group['gif_filter'] == 1 else '❌'), callback_data='ffgif_filters'))
    list_buttons.append(InlineKeyboardButton('Zip Filters %s' % ('✅' if group['zip_filter'] == 1 else '❌'), callback_data='ffzip_filters'))
    list_buttons.append(InlineKeyboardButton('TarGZ Filters %s' % ('✅' if group['targz_filter'] == 1 else '❌'), callback_data='fftargz_filters'))
    list_buttons.append(InlineKeyboardButton('JPG Filters %s' % ('✅' if group['jpg_filter'] == 1 else '❌'), callback_data='ffjpg_filters'))
    list_buttons.append(InlineKeyboardButton('Doc/x Filters %s' % ('✅' if group['docx_filter'] == 1 else '❌'), callback_data='ffdocx_filters'))
    list_buttons.append(InlineKeyboardButton('Apk Filters %s' % ('✅' if group['apk_filter'] == 1 else '❌'), callback_data='ffapk_filters'))
    list_buttons.append(InlineKeyboardButton("Close", callback_data='close'))
    menu = build_menu(list_buttons,2)
    if editkeyboard == False:
        keyboard_menu = bot.send_message(chat,"⚙️ Group Filters Settings\n\n📜 Group Name: <i>{}</i>\n🏷 ChatId: <code>{}</code>".format(chat_title,chat),reply_markup=InlineKeyboardMarkup(menu),parse_mode='HTML')
    if editkeyboard == True:
        keyboard_menu = bot.edit_message_reply_markup(chat,update.message.message_id,reply_markup=InlineKeyboardMarkup(menu))
    return keyboard_menu

@decorators.public.init
@decorators.admin.user_admin
@decorators.bot.check_is_admin
@decorators.delete.init
def init(update,context):
    keyboard_filters(update,context)

@decorators.admin.user_admin
def update_filters(update,context):
    query = update.callback_query
    chat = update.effective_message.chat_id
    group = GroupRepository().getById(chat)
    ###################################
    ####     SET CHAT FILTERS      ####
    ###################################
    if query.data.startswith("ff"):
        txt = query.data[2:]
        if txt == 'exe_filters':
            record = GroupRepository.EXE_FILTER
            row = group['exe_filter']
            if row == 0:
                update_db_settings(update, record, False)
                return keyboard_filters(query,context,True)
            else:
                update_db_settings(update, record, True)
                return keyboard_filters(query,context,True)
        if txt == 'zip_filters':
            record = GroupRepository.ZIP_FILTER
            row = group["zip_filter"]
            if row == 0:
                update_db_settings(update, record, False)
                return keyboard_filters(query,context,True)
            else:
                update_db_settings(update, record, True)
                return keyboard_filters(query,context,True)

        if txt== 'targz_filters':
            record = GroupRepository.TARGZ_FILTER
            row = group["targz_filter"]
            if row == 0:
                update_db_settings(update, record, False)
                return keyboard_filters(query,context,True)
            else:
                update_db_settings(update, record, True)
                return keyboard_filters(query,context,True)

        if txt == 'gif_filters':
            record = GroupRepository.GIF_FILTER
            row = group['gif_filter']
            if row == 0:
                update_db_settings(update, record, False)
                return keyboard_filters(query,context,True)
            else:
                update_db_settings(update, record, True)
                return keyboard_filters(query,context,True)

        if txt == 'jpg_filters':
            record = GroupRepository.JPG_FILTER
            row = group['jpg_filter']
            if row == 0:
                update_db_settings(update, record, False)
                return keyboard_filters(query,context,True)
            else:
                update_db_settings(update, record, True)
                return keyboard_filters(query,context,True)

        if txt == 'docx_filters':
            record = GroupRepository.DOCX_FILTER
            row = group['docx_filter']
            if row == 0:
                update_db_settings(update, record, False)
                return keyboard_filters(query,context,True)
            else:
                update_db_settings(update, record, True)
                return keyboard_filters(query,context,True)

        if txt == 'apk_filters':
            record = GroupRepository.APK_FILTER
            row = group['apk_filter']
            if row == 0:
                update_db_settings(update, record, False)
                return keyboard_filters(query,context,True)
            else:
                update_db_settings(update, record, True)
                return keyboard_filters(query,context,True)

        if txt == 'seall':
            record_TARGZ = GroupRepository.TARGZ_FILTER
            record_ZIP = GroupRepository.ZIP_FILTER
            record_EXE = GroupRepository.EXE_FILTER
            record_JPG = GroupRepository.JPG_FILTER
            record_APK = GroupRepository.APK_FILTER
            record_GIF = GroupRepository.GIF_FILTER
            record_DOCX = GroupRepository.DOCX_FILTER

            update_db_settings(update, record_TARGZ, False)
            update_db_settings(update, record_ZIP, False)
            update_db_settings(update, record_EXE, False)
            update_db_settings(update, record_JPG, False)
            update_db_settings(update, record_APK, False)
            update_db_settings(update, record_GIF, False)
            update_db_settings(update, record_DOCX, False)
            return keyboard_filters(query,context,True)

        if txt == 'deall':
            record_TARGZ = GroupRepository.TARGZ_FILTER
            record_ZIP = GroupRepository.ZIP_FILTER
            record_EXE = GroupRepository.EXE_FILTER
            record_JPG = GroupRepository.JPG_FILTER
            record_APK = GroupRepository.APK_FILTER
            record_GIF = GroupRepository.GIF_FILTER
            record_DOCX = GroupRepository.DOCX_FILTER

            update_db_settings(update, record_TARGZ, True)
            update_db_settings(update, record_ZIP, True)
            update_db_settings(update, record_EXE, True)
            update_db_settings(update, record_JPG, True)
            update_db_settings(update, record_APK, True)
            update_db_settings(update, record_GIF, True)
            update_db_settings(update, record_DOCX, True)
            return keyboard_filters(query,context,True)
