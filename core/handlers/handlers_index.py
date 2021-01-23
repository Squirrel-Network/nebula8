#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core import handlers
from core.commands import public
from telegram.ext import (MessageHandler as MH,Filters)

def test_handler(update,context):
    a = print("NO EXE ALLOWED")
    return a

def core_handlers(dsp):
    function = dsp.add_handler
    function(MH(Filters.text("@admin"), public.report.init))
    function(MH(Filters.document.exe, test_handler))
    function(MH(Filters.status_update.new_chat_members, handlers.welcome.init, run_async=True))
    function(MH(Filters.chat_type.groups, group_handlers, run_async=True))

def group_handlers(update,context):
    handlers.check_status_user.check_status(update, context)
    handlers.migrate_chat.init(update, context)