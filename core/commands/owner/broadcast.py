#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core import decorators
from core.utilities.message import message,messageWithId
from core.utilities.strings import Strings
from core.database.repository.group import GroupRepository
from telegram.error import BadRequest

@decorators.owner.init
def init(update, context):
    msg = update.message.text[2:].strip()
    rows = GroupRepository().getAll()
    for a in rows:
        id_groups = a['id_group']
        try:
            if msg == "":
                message(update,context,"You cannot send an empty message!")
            else:
                messageWithId(update,context,id_groups,msg)
        except BadRequest:
            message(update,context,Strings.ERROR_HANDLING)