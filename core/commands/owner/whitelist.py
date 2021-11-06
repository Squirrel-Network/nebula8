#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core import decorators
from core.utilities.message import message
from core.database.repository.superban import SuperbanRepository
from core.utilities.functions import user_reply_object
from core.utilities.menu import build_menu
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

@decorators.owner.init
@decorators.delete.init
def init(update,context):
    if update.message.reply_to_message:
        user = user_reply_object(update)
        row = SuperbanRepository().getWhitelistById(user.id)
        get_superban = SuperbanRepository().getById(user.id)
        if get_superban:
            buttons = []
            buttons.append(InlineKeyboardButton('Remove Superban', callback_data='removeBL'))
            buttons.append(InlineKeyboardButton('Close', callback_data='closed'))
            menu = build_menu(buttons,2)
            msg = "Attention the user is blacklisted! do you want to remove it?"
            update.message.reply_to_message.reply_text(msg, reply_markup=InlineKeyboardMarkup(menu),parse_mode='HTML')
        else:
            if row:
                message(update, context, "You have already whitelisted this user")
            else:
                user_username = "@"+user.username
                data = [(user.id, user_username)]
                SuperbanRepository().addWhitelist(data)
                message(update, context, "You have entered the user {} in the Whitelist".format(user_username))
    else:
        message(update, context, "This message can only be used in response to a user")


@decorators.owner.init
def remove_blacklist(update,context):
    query = update.callback_query
    user_id = query.message.reply_to_message.from_user.id
    if query.data == 'removeBL':
        user_id = query.message.reply_to_message.from_user.id
        row = SuperbanRepository().getById(user_id)
        if row:
            data = [(user_id)]
            SuperbanRepository().remove(data)
            msg = "I removed the superban to user <code>{}</code>".format(user_id)
            query.edit_message_text(msg,parse_mode='HTML')
        else:
            query.edit_message_text("Attention this user not super banned!!!",parse_mode='HTML')
    if query.data == 'closed':
        query.edit_message_text("You have closed the Menu", parse_mode='HTML')