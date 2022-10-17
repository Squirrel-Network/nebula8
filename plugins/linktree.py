#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core import decorators
from core.utilities.menu import build_menu
from core.database.repository.user import UserRepository
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.utilities.functions import user_object

@decorators.private.init
def init(update,context):
    bot = context.bot
    user = user_object(update)
    main_text = UserRepository().getLinktreeMainText(int(user.id))
    if main_text:
        get_buttons = UserRepository().getLinkTreeButtons(user.id)
        buttons = []
        for row in get_buttons:
            buttons.append(InlineKeyboardButton(text=row['button_text'], url=row['button_url']))
        menu = build_menu(buttons, 1)
        msg = main_text['main_text']
        bot.send_message(update.message.from_user.id, msg, reply_markup=InlineKeyboardMarkup(menu), parse_mode="HTML")
    else:
        bot.send_message(update.message.from_user.id,"You have not created any Linktree, Create your Linktree using the command [INSERT COMMAND HERE]", parse_mode="HTML")


def add_button(update,context):
    user = user_object(update)
    print(user)
