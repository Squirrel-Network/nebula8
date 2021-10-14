#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core import decorators
from core.utilities.message import message
from core.database.repository.group import GroupRepository

@decorators.admin.user_admin
@decorators.delete.init
def init(update,context):
    chat = update.effective_chat.id
    msg = update.message.text[8:].strip()
    if msg != "":
        data = [(msg,chat)]
        GroupRepository().insert_badword(data)
        message(update,context,"You have entered the forbidden word: [<b><i>{}</i></b>] in the database".format(msg))
    else:
        message(update, context, "You cannot enter an empty forbidden word!\nthe correct format of the command is: <code>/badword banana</code>")