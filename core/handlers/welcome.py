#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

import re
import json
from config import Config
from core import decorators
from languages.getLang import languages
from core.database.repository.group import GroupRepository
from core.database.repository.user import UserRepository
from core.database.repository.superban import SuperbanRepository
from core.utilities.message import message, reply_message
from core.utilities.regex import Regex
from core.utilities.functions import kick_user, ban_user, bot_object
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.handlers.logs import telegram_loggers
from core.utilities.menu import build_menu

LANGUAGE_KEYBOARD = [[
    InlineKeyboardButton("EN", callback_data='select_language_en'),
    InlineKeyboardButton("IT", callback_data='select_language_it')
    ]]

def has_arabic_character(string):
    arabic = re.search(Regex.HAS_ARABIC, string)
    return not not arabic

def save_user(member):
    # Save the user in the database and check that it exists if it exists and has changed nickname overwrite
    user = UserRepository().getById(member.id)
    if user:
        username = "@"+member.username
        data = [(username,member.id)]
        UserRepository().update(data)
    else:
        username = "@"+member.username
        default_warn = 0
        data = [(member.id,username,default_warn)]
        UserRepository().add(data)

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
        data = [(chat,default_welcome,default_buttons,default_rules,default_community,default_lang,default_set_welcome)]
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
    reply_markup = InlineKeyboardMarkup(LANGUAGE_KEYBOARD)
    msg = "Please select your preferred language\n\nPerfavore seleziona la tua lingua di preferenza"
    save_group(update)
    update.message.reply_text(msg,reply_markup=reply_markup)

@decorators.admin.user_admin
def select_language_en(update, context):
    chat = update.effective_message.chat_id
    msg = "You have selected the English language for your group\nRemember to make me admin in order to function properly!"
    query = update.callback_query
    query.answer()
    lang = "EN"
    data = [(lang,chat)]
    GroupRepository().update_language(data)
    query.edit_message_text(msg,parse_mode='HTML')

@decorators.admin.user_admin
def select_language_it(update, context):
    chat = update.effective_message.chat_id
    msg = "Hai selezionato la lingua italiana per il tuo gruppo\nRicordati di farmi admin per poter funzionare correttamente!"
    query = update.callback_query
    query.answer()
    lang = "IT"
    data = [(lang,chat)]
    GroupRepository().update_language(data)
    query.edit_message_text(msg,parse_mode='HTML')

def init(update, context):
    # Get settings
    chat = update.effective_message.chat_id
    group = GroupRepository().getById(chat)
    row = group['set_welcome']
    if row == 1:
        for member in update.message.new_chat_members:
            user = member.username
            user_first = member.first_name
            user_id = member.id
            chat_title = update.effective_chat.title
            chat_id = update.effective_chat.id
            bot = bot_object(update,context)

        if bot.id == user_id:
            welcome_bot(update,context)
            l_txt = "#Log <b>Bot added to group</b> {}\nId: <code>{}</code>".format(chat_title,chat_id)
            telegram_loggers(update,context,l_txt)
        elif user is None:
            kick_user(update, context)
            message(update,context,"<code>{}</code> set a username! You were kicked for safety!".format(user_id))
        elif is_in_blacklist(user_id):
            ban_user(update, context)
            message(update,context,"I got super banned <code>{}</code>".format(user_id))
        elif has_arabic_character(user_first):
            ban_user(update, context)
            message(update,context,"Non-Latin filter activated for the user <code>{}</code>".format(user_id))
        else:
            save_user(member)
            welcome_user(update,context,member)