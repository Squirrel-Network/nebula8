#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core import handlers
from core.commands import public
from telegram.ext import (MessageHandler as MH,Filters)
from core.utilities.functions import chat_object, user_object

def test_handler(update,context):
    a = print("NO EXE ALLOWED")
    return a

def terminal_handler(update):
    user = user_object(update)
    chat = chat_object(update)
    text = str(update.effective_message.text)
    msg = "FIRST_NAME: {}\nTG_ID: {}\nCHAT_ID: {}\nCHAT_TITLE: {}\nMESSAGE: {}".format(user.first_name,user.id,chat.id,chat.title,text)
    a = print(msg)
    return a

def core_handlers(dsp):
    function = dsp.add_handler
    function(MH(Filters.text("@admin"), public.report.init))
    function(MH(Filters.document.exe, test_handler))
    function(MH(Filters.status_update.new_chat_members, handlers.welcome.init, run_async=True))
    function(MH(Filters.chat_type.groups, group_handlers, run_async=True))

def group_handlers(update,context):
    handlers.check_status_user.check_status(update,context)
    terminal_handler(update)