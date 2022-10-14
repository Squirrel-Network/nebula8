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
    if str(update.effective_message.text).lower().startswith(".fiko"):
        msg = "I'm not GroupHelp! If you want to know who they are type /source"
        animation = "https://i.imgur.com/LP23P90.gif"
        message(update,context,msg,type='animation',img=animation)

@decorators.public.init
def nanachi(update,context):
    if str(update.effective_message.text).lower().startswith("nanachi"):
        msg = "Naaaa~~ 🐾"
        animation = "https://i.imgur.com/P9HXqM8.mp4"
        message(update,context,msg,type='animation',img=animation)