#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core import decorators
from core.utilities.message import message,messageWithId
from core.utilities.strings import Strings
from core.database.repository.community import CommunityRepository
from telegram.error import BadRequest

@decorators.owner.init
def init(update, context):
    msg = update.message.text[2:].strip()
    rows = CommunityRepository().getAll()
    for a in rows:
        id_groups = a['tg_group_id']
        try:
            if msg != "":
                messageWithId(update,context,id_groups,msg)
            else:
                message(update,context,"You cannot send an empty message!")
        except BadRequest:
            message(update,context,Strings.ERROR_HANDLING)