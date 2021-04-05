#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core import decorators
from core.database.repository.group import GroupRepository

@decorators.owner.init
def init(update,context):
    chat = update.effective_chat.id
    record_table = "gif_filter"
    data = [(1,chat)]
    GroupRepository().update_group_settings(record_table,data)