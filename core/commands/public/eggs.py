#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

"""
List of Easter Eggs
"""
from core import decorators
from core.utilities.message import message

@decorators.public.init
@decorators.delete.init
def egg_lost(update,context):
    message(update, context, "<code>4 8 15 16 23 42</code>")

@decorators.public.init
def egg_gh(update,context):
    bot = context.bot
    chat = update.effective_chat.id
    if str(update.effective_message.text).lower().startswith(".fiko"):
        animation = "https://i.imgur.com/LP23P90.gif"
        bot.sendAnimation(chat, animation, caption="I'm not GroupHelp! If you want to know who they are type /source")