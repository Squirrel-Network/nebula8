#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
import asyncio
from unicodedata import category
from core import decorators
from core.utilities.message import message,messageWithAsyncById
from core.utilities.strings import Strings
from core.database.repository.community import CommunityRepository
from core.database.repository.group import GroupRepository
from telegram.error import BadRequest, Unauthorized

loop = asyncio.get_event_loop()

@decorators.owner.init
def init(update, context):
    msg = update.message.text[2:].strip()
    rows = CommunityRepository().getAll()
    for a in rows:
        id_groups = a['tg_group_id']
        try:
            if msg != "":
                loop.run_until_complete(messageWithAsyncById(update,context,id_groups,2,msg))
            else:
                message(update,context,"You cannot send an empty message!")
        except (BadRequest,Unauthorized):
            category = a['type']
            message(update,context,Strings.ERROR_HANDLING.format(id_groups,category))

@decorators.owner.init
def global_broadcast(update, context):
    msg = update.message.text[3:].strip()
    rows = GroupRepository().getAll()
    for a in rows:
        id_groups = a['id_group']
        try:
            if msg != "":
                loop.run_until_complete(messageWithAsyncById(update,context,id_groups,2,msg))
            else:
                message(update,context,"You cannot send an empty message!")
        except (BadRequest,Unauthorized):
            message(update,context,Strings.ERROR_HANDLING.format(id_groups))