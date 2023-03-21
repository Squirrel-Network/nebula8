#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

#Send database backup into Telegram Private Channel
def send_backup(context):
    context.bot.send_document(chat_id='-1001316452992', document=open('/home/HgeyPaZppivx/internal_db_backup/nebula.sql', 'rb'))