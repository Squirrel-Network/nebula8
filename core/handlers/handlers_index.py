#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core import handlers
from telegram.ext import (
    MessageHandler as MH,
    CallbackQueryHandler as CQH,
    ConversationHandler as CH,
    Filters)

def core_handlers(dsp):
    function = dsp.add_handler
    function(MH(Filters.status_update.new_chat_members, handlers.welcome.init, run_async=True))
    function(MH(Filters.chat_type.groups, handlers.superban.init, run_async=True))
    function(CQH(handlers.welcome.select_language_en, pattern='select_language_en'))
    function(CQH(handlers.welcome.select_language_it, pattern='select_language_it'))