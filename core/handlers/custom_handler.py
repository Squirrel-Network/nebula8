#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core.utilities.functions import chat_object
from core.utilities.message import message
from core.database.repository.group import GroupRepository

def init(update,context):
    if str(update.effective_message.text).lower().startswith("nebula"):
        chat = chat_object(update)
        question = str(update.message.text.lower())
        row = GroupRepository().get_custom_handler([question,chat.id])
        if row:
            message(update,context,row['answer'])
        else:
            message(update,context,"Scusa non ho capito, riprova o crea il tuo comando")

    if str(update.effective_message.text).lower().startswith("!"):
        chat = chat_object(update)
        question = str(update.message.text.lower())
        row = GroupRepository().get_custom_handler([question,chat.id])
        if row:
            message(update,context,row['answer'])
        else:
            message(update,context,"Scusa non ho capito, riprova o crea il tuo comando")