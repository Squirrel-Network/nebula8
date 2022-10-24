#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core import decorators
from core.database.repository.community import CommunityRepository
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.utilities.menu import build_menu

@decorators.owner.init
def groups(update,context):
    bot = context.bot
    chat = update.effective_chat.id
    list_buttons = []
    rows = CommunityRepository().getCommunityGroups()
    for link in rows:
        list_buttons.append(InlineKeyboardButton(text=link['tg_group_name'], url=link['tg_group_link']))
    menu = build_menu(list_buttons,2)
    main_text = "=== 🐿[SN] Squirrel Network Official 🐿===\nTo participate in the Network contact:\n@TheLonelyAdventurer\n@SteelManITA\n@BluLupo"
    bot.send_message(chat,text=main_text,reply_markup=InlineKeyboardMarkup(menu), parse_mode="HTML")

@decorators.owner.init
def channels(update,context):
    bot = context.bot
    chat = update.effective_chat.id
    list_buttons = []
    rows = CommunityRepository().getCommunityChannels()
    for link in rows:
        list_buttons.append(InlineKeyboardButton(text=link['tg_group_name'], url=link['tg_group_link']))
    menu = build_menu(list_buttons,2)
    main_text = "=== 🐿[SN] Squirrel Network Official 🐿===\nTo participate in the Network contact:\n@TheLonelyAdventurer\n@SteelManITA\n@BluLupo"
    bot.send_message(chat,text=main_text,reply_markup=InlineKeyboardMarkup(menu), parse_mode="HTML")