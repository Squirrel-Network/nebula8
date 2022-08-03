#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core import decorators
from languages.getLang import languages
from core.utilities.message import message

@decorators.admin.user_admin
@decorators.bot.check_can_delete
@decorators.delete.init
def init(update,context):
    languages(update,context)
    msg = update.message.text[4:].strip()
    if msg != "":
        message(update, context, msg, 'HTML', 'message', None, None)
    else:
        message(update, context, languages.say_error, 'HTML', 'message', None, None)