#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

import plugins
from telegram.ext import (
    CommandHandler as CMH,
    MessageHandler as MH,
    CallbackQueryHandler as CQH,
    ConversationHandler as CH,
    Filters)

def function_plugins(dsp):
    function = dsp.add_handler
    function(CMH('distro',plugins.distrowatch.init))
    function(CMH('google',plugins.google.init))