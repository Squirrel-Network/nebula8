#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core.utilities.constants import PERM_FALSE

def init(update,context):
    context.job_queue.run_repeating(callback_night,interval=10.0,first=0.0, name="[NIGHT_SCHEDULE_JOB]",context=update.effective_chat.id)

def callback_night(context):
    chat_id = context.job.context
    context.bot.send_message(chat_id=chat_id, text="TEST_NIGHT_SCHEDULE")
    context.bot.set_chat_permissions(chat_id, PERM_FALSE)
    print(chat_id)