#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core import decorators
from core.utilities.message import message
from core.utilities.functions import chat_object
from core.database.repository.community import CommunityRepository
from core.utilities.menu import build_menu
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

@decorators.owner.init
def init(update,context):
    bot = context.bot
    chat = chat_object(update)
    if chat.type == 'supergroup':
        row = CommunityRepository().getById(chat.id)
        if row:
            data = [(chat.title,chat.id)]
            CommunityRepository().update(data)
            message(update,context,"Update Community")
        else:
            buttons = []
            buttons.append(InlineKeyboardButton('IT', callback_data='commIT'))
            buttons.append(InlineKeyboardButton('EN', callback_data='commEN'))
            buttons.append(InlineKeyboardButton('Close', callback_data='closeMenu'))
            menu = build_menu(buttons,2)
            bot.send_message(chat_id=update.effective_chat.id,text="Please select the language of the community",reply_markup=InlineKeyboardMarkup(menu))
    else:
        message(update,context,"Attention! this command can only be used in public supergroups!")
        #data = [(chat.title,chat.id,link)]
        #CommunityRepository().add(data)
        #message(update,context,"Insert Community")

@decorators.owner.init
def callback_community(update,context):
    query = update.callback_query
    if query.data.startswith("comm"):
        lang_set = query.data[4:]
        type_community = query.message.chat.type
        chat_id = query.message.chat_id
        chat_title = query.message.chat.title
        chat_username = query.message.chat.username
        print(chat_username)
        link = "https://t.me/{}".format(chat_username)
        data = [(chat_title,chat_id,link,lang_set,type_community)]
        print(data)