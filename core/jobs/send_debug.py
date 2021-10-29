#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

#Send debug.log into Dev_Channel
def send_log(context):
    context.bot.send_document(chat_id='-1001540824311', document=open('debug.log', 'rb'))