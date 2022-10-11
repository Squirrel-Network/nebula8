#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core import decorators
from core.utilities.menu import build_menu
from core.utilities.message import message
from core.utilities.functions import user_reply_object
from core.database.repository.user import UserRepository
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

@decorators.owner.init
@decorators.delete.init
def init(update,context):
    if update.message.reply_to_message:
        user = user_reply_object(update)
        user_id = user.id
        username = "@"+user.username
        row = UserRepository().getOwnerById(user.id)
        list_buttons = []
        if row:
            list_buttons.append(InlineKeyboardButton('❌ Remove', callback_data='OwnerRemove'))
            list_buttons.append(InlineKeyboardButton("🗑 Close", callback_data='close'))
            menu = build_menu(list_buttons, 1)
            update.message.reply_to_message.reply_text('{} This owner already exists in the database'.format(username),reply_markup=InlineKeyboardMarkup(menu),parse_mode='HTML')
        else:
            data = [(user_id, username)]
            UserRepository().add_owner(data)
            message(update,context, "You have entered {} [<code>{}</code>] a new owner in the database!\nRestart the Bot!".format(username,user_id))
    else:
        message(update,context, "Error! This command should be used in response to the user!")

@decorators.owner.init
def update_owner(update,context):
    query = update.callback_query
    user = query.message.reply_to_message.from_user
    if query.data == 'OwnerRemove':
        data = [(user.id)]
        UserRepository().remove_owner(data)
        query.edit_message_text("You have removed owner {} [<code>{}</code>] from the database".format(user.first_name,user.id), parse_mode='HTML')