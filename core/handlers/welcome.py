#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
import time
import datetime
import re
import json
import requests
from config import Config
from core.database.repository.group import GroupRepository
from core.database.repository.user import UserRepository
from core.database.repository.superban import SuperbanRepository
from core.utilities.message import message, reply_message
from core.utilities.regex import Regex
from core.utilities.functions import kick_user, ban_user, bot_object, mute_user_by_id
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.utils.helpers import mention_html
from core.handlers.logs import telegram_loggers
from core.utilities.menu import build_menu
from core.utilities.strings import Strings

def get_owner_list() -> list:
    rows = UserRepository().getOwners()
    arr_owners = []
    for a in rows:
        owners = int(a['tg_id'])
        arr_owners.append(owners)
    return arr_owners

OWNER_LIST = get_owner_list()

def has_arabic_character(string):
    arabic = re.search(Regex.HAS_ARABIC, string)
    return not not arabic

def has_cirillic_character(string):
    cirillic = re.search(Regex.HAS_CIRILLIC, string)
    return not not cirillic

def has_chinese_character(string):
    chinese = re.search(Regex.HAS_CHINESE, string)
    return not not chinese

def has_zoophile(string):
    zoophile = re.search(Regex.HAS_ZOOPHILE, string)
    return not not zoophile

def save_user(member, chat):
    # Save the user in the database and check that it exists if it exists and has changed nickname overwrite
    user = UserRepository().getById(member.id)
    username = "@"+member.username
    default_count_warn = 0
    current_time = datetime.datetime.utcnow().isoformat()
    if user:
        data = [(username,current_time,member.id)]
        UserRepository().update(data)
    else:
        data = [(member.id,username,current_time,current_time)]
        UserRepository().add(data)
    data_mtm = [(member.id, chat, default_count_warn)]
    UserRepository().add_into_mtm(data_mtm)

def save_group(update):
    chat = update.effective_message.chat_id
    chat_title = update.effective_chat.title
    record = GroupRepository.SET_GROUP_NAME
    group = GroupRepository().getById(chat)
    if group:
        data = [(chat_title, chat)]
        GroupRepository().update_group_settings(record, data)
    else:
        dictionary = {
            "id_group": chat,
            "group_name": chat_title,
            "welcome_text": Config.DEFAULT_WELCOME.format("{username}","{chat}"),
            "welcome_buttons": '{"buttons": [{"id": 0,"title": "Bot Logs","url": "https://t.me/nebulalogs"}]}',
            "rules_text": Config.DEFAULT_RULES,
            "community": 0,
            "languages": Config.DEFAULT_LANGUAGE,
            "set_welcome": 1,
            "max_warn": 3,
            "set_silence": 0,
            "exe_filter": 0,
            "block_new_member": 0,
            "set_arabic_filter": 0,
            "set_cirillic_filter": 0,
            "set_chinese_filter": 0,
            "set_user_profile_picture": 0,
            "gif_filter": 0,
            "set_cas_ban": 1,
            "type_no_username": 1,
            "log_channel": Config.DEFAULT_LOG_CHANNEL,
            "group_photo": 'https://naos.hersel.it/group_photo/default.jpg',
            "total_users": 0,
            "zip_filter": 0,
            "targz_filter": 0,
            "jpg_filter": 0,
            "docx_filter": 0,
            "apk_filter": 0,
            "zoophile_filter": 1,
            "sender_chat_block": 1,
            "spoiler_block": 0,
            "set_no_vocal": 0,
            "set_antiflood": 1
        }
        GroupRepository().add_with_dict(dictionary)

def is_in_blacklist(uid):
    return not not SuperbanRepository().getById(uid)

def welcome_user(update, context, member):
    # Check that the welcome exists on the database if there is no Default Welcome
    chat = update.effective_message.chat_id

    group = GroupRepository().getById(chat)
    if group is not None:
        parsed_message = group['welcome_text'].replace('{first_name}',
        member.first_name).replace('{chat}',
        update.message.chat.title).replace('{username}',
        "@"+member.username).replace('{mention}',mention_html(member.id, member.first_name)).replace('{userid}',str(member.id))
        format_message = "{}".format(parsed_message)
        buttons = GroupRepository().getById(chat)
        try:
            welcome_buttons = buttons['welcome_buttons']
            format_json = json.loads(welcome_buttons)
            x = format_json['buttons']
            arr_buttons = []
            for a in x:
                title = a['title']
                url = a['url']
                arr_buttons.append(InlineKeyboardButton(text=title, url=url))
            menu = build_menu(arr_buttons, 2)
            update.message.reply_text(format_message,reply_markup=InlineKeyboardMarkup(menu),parse_mode='HTML')
        except ValueError:
            reply_message(update,context,format_message)
    else:
        chat_title = update.effective_chat.title
        default_welcome = Config.DEFAULT_WELCOME.format("@"+member.username,chat_title)
        reply_message(update, context,default_welcome)


def welcome_bot(update, context):
    save_group(update)
    update.message.reply_text(Strings.WELCOME_BOT.format(Config.VERSION,Config.VERSION_NAME))

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
        type_no_username = group['type_no_username']
        zoophile_filter = group["zoophile_filter"]
    else:
        row = 1
        block_user = 0
        arabic_filter =  1
        cirillic_filter = 1
        chinese_filter = 1
        user_profile_photo = 0
        zoophile_filter = 1

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
            # Welcome the bot when it is added
            if bot.id == user_id:
                l_txt = "#Log <b>Bot added to group</b> {}\nId: <code>{}</code>".format(chat_title,chat_id)
                telegram_loggers(update,context,l_txt)
                welcome_bot(update, context)
            # Kicked user because username field is empty
            elif user is None:
                if type_no_username == 1:
                    message(update,context,'<a href="tg://user?id={}">{}</a> set an <b>username!</b> You were kicked for safety!'.format(user_id,user_first))
                    time.sleep(2)
                    kick_user(update, context)
                elif type_no_username == 2:
                    message(update,context,'<a href="tg://user?id={}">{}</a> set an <b>username!</b>'.format(user_id,user_first))
                elif type_no_username == 3:
                    message(update,context,'<a href="tg://user?id={}">{}</a> set an <b>username!</b> You were Muted for safety!'.format(user_id,user_first))
                    mute_user_by_id(update, context, member.id, True)
                elif type_no_username == 4:
                    ban_user(update,context)
                    message(update,context,'<a href="tg://user?id={}">{}</a> was banned because they did not have an username'.format(user_id,user_first))
                elif type_no_username == 5:
                    kick_user(update, context)
                elif has_zoophile(user_first) and zoophile_filter == 1:
                    ban_user(update, context)
                    message(update, context, "Nebula's automatic system intercepted a <b>zoophile!</b>\nI banned user {}".format(mention_html(user_id, user_first)))
                else:
                    arr_buttons = []
                    arr_buttons.append(InlineKeyboardButton(text="Bot_logs", url="https://t.me/nebulalogs"))
                    menu = build_menu(arr_buttons, 2)
                    main_msg = "Welcome {} in {}".format(mention_html(member.id, member.first_name),chat_title)
                    update.message.reply_text(main_msg,reply_markup=InlineKeyboardMarkup(menu),parse_mode='HTML')
                    print("No action even if you don't have a username")
            # They ban the user because he is blacklisted
            elif is_in_blacklist(user_id):
                ban_user(update, context)
                message(update, context, 'I got super banned <a href="tg://user?id={}">{}</a> [{}]'.format(user_id,user_first,user_id))
            # They ban the user because he doesn't have a profile picture
            elif user_photo.total_count == 0 and user_profile_photo == 1:
                kick_user(update, context)
                message(update,context,'<a href="tg://user?id={}">{}</a> set a profile picture! You were kicked for safety!'.format(user_id,user_first))
            # Banned user with arabic characters
            elif has_arabic_character(user_first) and arabic_filter == 1:
                ban_user(update, context)
                message(update,context,"Non-Latin filter activated for the user <code>{}</code>".format(mention_html(user_id, user_first)))
            # Banned user with cirillic characters
            elif has_cirillic_character(user_first) and cirillic_filter == 1:
                ban_user(update, context)
                message(update,context,"Non-Latin filter activated for the user <code>{}</code>".format(mention_html(user_id, user_first)))
            # Banned user with chinese characters
            elif has_chinese_character(user_first) and chinese_filter == 1:
                ban_user(update, context)
                message(update,context,"Non-Latin filter activated for the user <code>{}</code>".format(mention_html(user_id, user_first)))
            # Banned user with Zoophile characters
            elif has_zoophile(user_first) and zoophile_filter == 1:
                ban_user(update, context)
                message(update, context, "Nebula's automatic system intercepted a <b>zoophile!</b>\nI banned user {}".format(mention_html(user_id, user_first)))
            # Welcome for bot owner
            elif user_id in OWNER_LIST:
                message(update, context, 'The bot operator <a href="tg://user?id={}">{}</a> has just joined the group'.format(user_id,user_first))
            else:
                save_user(member, chat_id)
                welcome_user(update,context,member)