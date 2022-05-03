#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core.utilities.functions import chat_object, user_object
from core.utilities.message import message
from core.database.repository.group import GroupRepository
from telegram.utils.helpers import mention_html

def init(update,context):
    if str(update.effective_message.text).lower().startswith("nebula"):
        chat = chat_object(update)
        user = user_object(update)
        question = str(update.message.text.lower())
        row = GroupRepository().get_custom_handler([question,chat.id])
        if row:
            parsed_message = row['answer'].replace('{first_name}',
            user.first_name).replace('{chat}',
            update.message.chat.title).replace('{username}',
            "@"+user.username).replace('{mention}',mention_html(user.id, user.first_name)).replace('{userid}',str(user.id))
            text = "{}".format(parsed_message)
            message(update,context,text)
        else:
            return

    if str(update.effective_message.text).lower().startswith("!"):
        chat = chat_object(update)
        user = user_object(update)
        question = str(update.message.text.lower())
        row = GroupRepository().get_custom_handler([question,chat.id])
        if row:
            parsed_message = row['answer'].replace('{first_name}',
            user.first_name).replace('{chat}',
            update.message.chat.title).replace('{username}',
            "@"+user.username).replace('{mention}',mention_html(user.id, user.first_name)).replace('{userid}',str(user.id))
            text = "{}".format(parsed_message)
            message(update,context,text)
        else:
            return