#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core import decorators
from languages.getLang import languages
from core.utilities.message import message
from core.utilities.functions import chat_object
from core.database.repository.group import GroupRepository

@decorators.admin.user_admin
@decorators.delete.init
def init(update,context):
    chat = chat_object(update)
    msg = update.message.text[8:].strip()
    if msg != "":
        data = [(msg,chat.id)]
        GroupRepository().insert_badword(data)
        message(update,context,languages.badlist_add.format(msg))
    else:
        message(update, context,languages.badlist_add_empty)

@decorators.admin.user_admin
@decorators.delete.init
def badlist(update,context):
    chat = chat_object(update)
    languages(update,context)
    rows = GroupRepository().get_badwords_group(chat.id)
    if rows:
        string = ""
        for row in rows:
            string += "▪️ {}\n".format(row['word'])
        message(update,context,languages.badlist_text.format(chat.title,string))
    else:
        message(update,context,languages.badlist_empty)
