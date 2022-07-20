#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

#Send debug.log into Dev_Channel
from core.database.repository.group import GroupRepository

def query(context):
    GroupRepository().job_nebula_updates()
    context.send_message(chat_id='-1001540824311', text="I ran the nebula_updates table cleanup query")