#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core import decorators
from languages.getLang import languages
from core.utilities.message import message

@decorators.admin.user_admin
@decorators.delete.init
def init(update,context):
    languages(update,context)
    msg = update.message.text[4:].strip()
    if msg != "":
        message(update,context,msg)
    else:
        message(update,context,languages.say_error)