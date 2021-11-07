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

@decorators.admin.user_admin
@decorators.delete.init
def badlist(update,context):
    chat = update.effective_chat.id
    rows = GroupRepository().get_badwords_group(chat)
    if rows:
        string = ""
        for row in rows:
            string += "{}\n".format(row['word'])
        message(update,context,"Badwords List:\n{}".format(string))
    else:
        message(update,context,"There is no badword for this group.\nYou can add a badword with the command <code>/badword word</code>")
