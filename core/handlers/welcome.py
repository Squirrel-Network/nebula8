#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

import re
import json
from config import Config
from core.database.repository.group import GroupRepository
from core.database.repository.user import UserRepository
from core.database.repository.superban import SuperbanRepository
from core.utilities.message import message, reply_message
from core.utilities.regex import Regex
from core.utilities.functions import kick_user, ban_user, bot_object
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.handlers.logs import telegram_loggers
from core.utilities.menu import build_menu

OWNER_LIST = list(Config.OWNER.values())

def has_arabic_character(string):
    arabic = re.search(Regex.HAS_ARABIC, string)
    return not not arabic

def has_cirillic_character(string):
    arabic = re.search(Regex.HAS_CIRILLIC, string)
    return not not arabic

def has_chinese_character(string):
    arabic = re.search(Regex.HAS_CHINESE, string)
    return not not arabic

def save_user(member, chat):
    # Save the user in the database and check that it exists if it exists and has changed nickname overwrite
    user = UserRepository().getById(member.id)
    username = "@"+member.username
    default_count_warn = 0
    if user:
        data = [(username,member.id)]
        UserRepository().update(data)
    else:
        data = [(member.id,username,default_count_warn)]
        UserRepository().add(data)
    data_mtm = [(member.id, chat, default_count_warn)]
    UserRepository().add_into_mtm(data_mtm)

def save_group(update):
    chat = update.effective_message.chat_id
    group = GroupRepository().getById(chat)
    if group:
        print('update group')
        #data = [(chat,chat)]
        #GroupRepository().update(data)
    else:
        default_welcome = Config.DEFAULT_WELCOME.format("{username}","{chat}")
        default_buttons = ""
        default_rules = Config.DEFAULT_RULES
        default_lang = Config.DEFAULT_LANGUAGE
        default_community = 0
        default_set_welcome = 1
        default_max_warn = 3
        default_global_silence = 0
        default_exe_filter = 0
        default_block_user = 0
        default_arabic_filter = 1
        default_cirillic_filter = 1
        default_chinese_filter = 1
        default_user_profile_photo = 0
        default_gif_filter = 0

        data = [(
            chat,default_welcome,
            default_buttons,
            default_rules,
            default_community,
            default_lang,
            default_set_welcome,
            default_max_warn,
            default_global_silence,
            default_exe_filter,
            default_block_user,
            default_arabic_filter,
            default_cirillic_filter,
            default_chinese_filter,
            default_user_profile_photo,
            default_gif_filter
            )]
        GroupRepository().add(data)

def is_in_blacklist(uid):
    return not not SuperbanRepository().getById(uid)

def welcome_user(update, context, member):
    # Check that the welcome exists on the database if there is no Default Welcome
    chat = update.effective_message.chat_id

    group = GroupRepository().getById(chat)
    if group is not None:
        parsed_message = group['welcome_text'].replace(
            '{first_name}',
            update.message.from_user.first_name).replace('{chat}',
            update.message.chat.title).replace('{username}',
            "@"+member.username
        )
        format_message = "{}".format(parsed_message)
        buttons = GroupRepository().getById(chat)
        try:
            welcome_buttons = buttons['welcome_buttons']
            format_json = json.loads(welcome_buttons)
            arr_buttons = []
            for key, value in format_json.items():
                arr_buttons.append(InlineKeyboardButton(text=key, url=value))
            menu = build_menu(arr_buttons, 2)
            update.message.reply_text(format_message,reply_markup=InlineKeyboardMarkup(menu),parse_mode='HTML')
        except ValueError:
            reply_message(update,context,format_message)
    else:
        chat_title = update.effective_chat.title
        default_welcome = Config.DEFAULT_WELCOME.format("@"+member.username,chat_title)
        reply_message(update, context,default_welcome)


def welcome_bot(update, context):
    msg = "Please select your language => /lang \n\nRemember to make me administrator to work properly"
    save_group(update)
    update.message.reply_text(msg)

def init(update, context):
    # Get settings
    chat = update.effective_message.chat_id
    group = GroupRepository().getById(chat)

    if group:
        row = group['set_welcome']
        block_user = group['block_new_member']
        arabic_filter = group['set_arabic_filter']
        cirillic_filter = group['set_cirillic_filter']
        chinese_filter = group['set_chinese_filter']
        user_profile_photo = group['set_user_profile_picture']
    else:
        row = 1
        block_user = 0
        arabic_filter =  1
        cirillic_filter = 1
        chinese_filter = 1
        user_profile_photo = 0

    if row == 0 and block_user == 1:
        for member in update.message.new_chat_members:
            kick_user(update, context)
            message(update, context, "<b>#Automatic Handler:</b> Kick User for group protection")

    if row == 1 and row is not None:
        for member in update.message.new_chat_members:
            user = member.username
            user_first = member.first_name
            user_id = member.id
            chat_title = update.effective_chat.title
            chat_id = update.effective_chat.id
            bot = bot_object(update,context)
            user_photo = member.get_profile_photos(member.id)

        if bot.id == user_id:
            welcome_bot(update, context)
            l_txt = "#Log <b>Bot added to group</b> {}\nId: <code>{}</code>".format(chat_title,chat_id)
            telegram_loggers(update,context,l_txt)
        # Banned user because username field is empty
        elif user is None:
            kick_user(update, context)
            message(update,context,"<code>{}</code> set a username! You were kicked for safety!".format(user_id))
        elif user_photo.total_count == 0 and user_profile_photo == 1:
            kick_user(update, context)
            message(update,context,"<code>{}</code> set a profile picture! You were kicked for safety!".format(user_id))
        elif is_in_blacklist(user_id):
            ban_user(update, context)
            message(update, context, 'I got super banned <a href="tg://user?id={}">{}</a>'.format(user_id,user_first))
        # Banned user with arabic characters
        elif has_arabic_character(user_first) and arabic_filter == 1:
            ban_user(update, context)
            message(update,context,"Non-Latin filter activated for the user <code>{}</code>".format(user_id))
        # Banned user with cirillic characters
        elif has_cirillic_character(user_first) and cirillic_filter == 1:
            ban_user(update, context)
            message(update,context,"Non-Latin filter activated for the user <code>{}</code>".format(user_id))
        # Banned user with chinese characters
        elif has_chinese_character(user_first) and chinese_filter == 1:
            ban_user(update, context)
            message(update,context,"Non-Latin filter activated for the user <code>{}</code>".format(user_id))
        elif user_id in OWNER_LIST:
            message(update, context, 'The bot operator <a href="tg://user?id={}">{}</a> has just joined the group'.format(user_id,user_first))
        else:
            save_user(member, chat_id)
            welcome_user(update,context,member)