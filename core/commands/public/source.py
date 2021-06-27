#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from config import Config
from core import decorators
from core.utilities.message import message
from core.utilities.functions import bot_object
from core.utilities.strings import Strings

@decorators.delete.init
def init(update,context):
    bot = bot_object(update,context)
    version = Config.VERSION
    version_name = Config.VERSION_NAME
    repo = Config.REPO
    format_message = Strings.SOURCE.format("@"+bot.username,version,version_name,repo)
    message(update,context,format_message)