#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core import decorators
from core.utilities.message import message
from languages.getLang import languages
from core.database.repository.group import GroupRepository
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.utilities.menu import build_menu
import json

def _remove_button(group_id, btn_id):
    """
     group_id, int indicating the id of the group
     btn_id, json button id to remove
    """
    # select
    group_record = GroupRepository().getById(group_id)
    welcome_btns = group_record['welcome_buttons']
    welcome_btns = json.loads(welcome_btns)['buttons']

    new_welcome_btns = [btn for btn in welcome_btns if btn['id'] != int(btn_id)]

    # insert
    welcome_btns_text = json.dumps({"buttons": new_welcome_btns})
    GroupRepository().updateWelcomeButtonsByGroupId(group_id, welcome_btns_text)

def _add_button(group_id, btn):
    """
    group_id, int indicating the id of the group
    btn, dict representing a json button
    """
    # select
    group_record = GroupRepository().getById(group_id)
    welcome_btns = group_record['welcome_buttons']
    welcome_btns = (json.loads(welcome_btns))['buttons']

    # add
    if len(welcome_btns) == 0:
        btn['id'] = 0
    else:
        btn['id'] = welcome_btns[-1]['id'] + 1

    welcome_btns.append(btn)

    # insert
    welcome_btns_text = json.dumps({"buttons": welcome_btns})
    GroupRepository().updateWelcomeButtonsByGroupId(group_id, welcome_btns_text)

@decorators.admin.user_admin
@decorators.delete.init
def set_welcome_buttons(update, context):
    try:
        cmd_args = update.message.text[16:].strip().split()
        action = cmd_args[0]
        group_id = update.effective_chat.id

        # Add Welcome Buttons /welcomebuttons add "title" "url"
        if action == 'add':
            title = cmd_args[1][1:-1]
            url = cmd_args[2][1:-1]
            button = {'title': title, 'url': url}

            _add_button(group_id, button)
            message(update, context, "You have added a button to the welcome!")
        # Remove Welcome Buttons /welcomebuttons remove "buttonid"
        elif action == 'remove':
            button_id = cmd_args[1][1:-1]
            _remove_button(group_id, button_id)
            message(update, context, "You have removed the button with id: <code>{}</code>".format(button_id))
        # If no action has been taken, this error is returned
        else:
            message(update, context, "The action you requested is incorrect type <code>add</code> or <code>remove</code>")
    except IndexError:
        # List Welcome Buttons /welcomebuttons with no args
            chat = update.effective_message.chat_id
            buttons = GroupRepository().getById(chat)
            welcome_buttons = buttons['welcome_buttons']
            format_json = json.loads(welcome_buttons)
            x = format_json['buttons']
            options = ""
            for a in x:
                if 'id' in a:
                    button_id = a['id']
                else:
                    button_id = -1
                title = a['title']
                url = a['url']
                options += "Button Id: <code>{}</code>\n".format(button_id)
                options += "Button Text: <b>{}</b>\n".format(title)
                options += "Button Url: <code>{}</code>\n\n\n".format(url)
            message(update, context, options)

@decorators.admin.user_admin
@decorators.delete.init
def init(update, context):
    languages(update,context)
    record = GroupRepository.SET_WELCOME_TEXT
    chat = update.effective_chat.id
    msg = update.message.text[8:].strip()
    if msg != "":
        data = [(msg, chat)]
        GroupRepository().update_group_settings(record, data)
        message(update, context, languages.set_welcome_help)
    else:
        message(update, context, languages.set_welcome_main)


@decorators.admin.user_admin
@decorators.delete.init
def set_type_no_username(update, context):
    bot = context.bot
    chat = update.effective_message.chat_id
    buttons = []
    buttons.append(InlineKeyboardButton('Kick Only', callback_data='tpnu1'))
    buttons.append(InlineKeyboardButton('Message Only', callback_data='tpnu2'))
    buttons.append(InlineKeyboardButton('Mute Only', callback_data='tpnu3'))
    buttons.append(InlineKeyboardButton('Close', callback_data='closeMenu'))
    menu = build_menu(buttons,3)
    bot.send_message(chat,"No Username Filter Settings", reply_markup=InlineKeyboardMarkup(menu),parse_mode='HTML')


@decorators.admin.user_admin
def update_set_tpnu(update, context):
    query = update.callback_query
    if query.data.startswith("tpnu"):
        chat_id = query.message.chat_id
        tpnu_set = query.data[4:]
        record = GroupRepository.SET_TPNU
        data = [(tpnu_set,chat_id)]
        GroupRepository().update_group_settings(record, data)
        text = "You have set the filter to <code>{}</code>\nLegend:\n<code>1 == Kick\n2 == Message\n3 == Mute</code>".format(tpnu_set)
        query.edit_message_text(text, parse_mode='HTML')
