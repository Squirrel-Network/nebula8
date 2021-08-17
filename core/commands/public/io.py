#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core import decorators
from core.utilities.message import message
from core.utilities.functions import user_object
from core.database.repository.superban import SuperbanRepository

@decorators.private.init
@decorators.delete.init
def init(update,context):
    user = user_object(update)
    nickname = "@"+ user.username
    superban = SuperbanRepository().getById(user.id)
    if superban:
        msg = "<b>User id:</b> <code>{}</code>\n<b>Nickname:</b> {}\n<b>Blacklist:</b> ✅".format(user.id, nickname or user.first_name)
    else:
        msg = "<b>User id:</b> <code>{}</code>\n<b>Nickname:</b> {}\n<b>Blacklist:</b> ❌".format(user.id, nickname or user.first_name)
    message(update,context,msg)