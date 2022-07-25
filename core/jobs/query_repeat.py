#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

#Send debug.log into Dev_Channel
from core.database.repository.group import GroupRepository

def query(context):
    bot = context.bot
    chat = '-1001540824311'
    GroupRepository().job_nebula_updates()
    bot.send_message(chat,text="[DEBUG LOGGER] I ran the nebula_updates table cleanup query",parse_mode='HTML')