#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core import handlers
from core import jobs
from core.commands import public
from telegram.ext import (MessageHandler as MH,Filters)
from core.utilities.constants import FOUR_HOUR

def core_handlers(dsp):
    function = dsp.add_handler
    function(MH(Filters.status_update.new_chat_members, handlers.welcome.init, run_async=True))
    function(MH(Filters.chat_type, group_handlers, run_async=True))

def group_handlers(update,context):
    handlers.check_status_user.check_status(update, context)
    handlers.check_status_chat.check_status(update, context)
    handlers.check_status_chat.check_updates(update)
    public.report.init(update,context)
    public.eggs.egg_gh(update,context)
    handlers.filters_chat.init(update, context)
    handlers.logs.set_log_channel(update,context)

def jobs_handlers(job):
    job.run_repeating(jobs.send_debug.send_message_job,interval=FOUR_HOUR,first=0.0, name="[DEBUG_LOG_JOB]")