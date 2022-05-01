#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core.utilities.functions import chat_object
from core.database.repository.group import GroupRepository

def init(update,context):
    if str(update.effective_message.text).lower().startswith("nebula"):
        chat = chat_object(update)
        question = str(update.message.text).lower()
        print(question)
        data = (question,chat.id)
        row = GroupRepository().get_custom_handler(data)
        if row:
            print(row['answer'])
            print(chat.id)