#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

import time
from core import decorators

#from core.utilities.message import message
#from core.utilities.functions import user_object
#from telegram.utils.helpers import mention_html
from core.utilities.functions import chat_status_object_by_id
from core.database.repository.group import GroupRepository
from telegram.error import Unauthorized
#from telegram import InlineKeyboardButton, InlineKeyboardMarkup
#from core.utilities.menu import build_menu


@decorators.owner.init
def init(update,context):
    print("TEST")

#@decorators.owner.init
#def init(update,context):
    #context.job_queue.run_repeating(callback_all_chat,interval=10.0,first=0.0, name="[NIGHT_SCHEDULE_JOB]",context=update.effective_chat.id)

#@decorators.owner.init
#def init(update,context):
    #context.job_queue.run_repeating(callback_all_chat, interval=20.0, first=0.0, name="[GET_STATUS_ALL_GROUPS]")

def callback_all_chat(context):
    rows = GroupRepository().getAll()
    for a in rows:
        try:
            chat_id = a['id_group']
            x = chat_status_object_by_id(context,chat_id)
            time.sleep(2)
            print(x)
        except Unauthorized:
            print("NOT FOUND")

def callback_night(context):
    chat_id = context.job.context
    context.bot.send_message(chat_id=chat_id, text="TEST_NIGHT_SCHEDULE")
    print(chat_id)

def callback_chat(context):
    chat_id = context.job.context
    print(chat_id)
    #x = chat_status_object_by_id(context,chat_id)
    #context.bot.send_message(chat_id=chat_id, text="TEST_NIGHT_SCHEDULE")
    #print(x)