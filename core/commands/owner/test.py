#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core import decorators
from core.utilities.message import message
from core.utilities.functions import user_object
from telegram.utils.helpers import mention_html

@decorators.owner.init
def init(update, context):
    user = user_object(update)
    message(update, context, "{}".format(mention_html(user.id, user.first_name)))
#def init(update,context):
    #context.job_queue.run_repeating(callback_night,interval=10.0,first=0.0, name="[NIGHT_SCHEDULE_JOB]",context=update.effective_chat.id)

def callback_night(context):
    chat_id = context.job.context
    context.bot.send_message(chat_id=chat_id, text="TEST_NIGHT_SCHEDULE")
    print(chat_id)