#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core.commands import public ,admin, owner
from telegram.ext import (CommandHandler as CMH,CallbackQueryHandler as CQH,MessageHandler as MH,Filters)

def user_command(dsp):
    function = dsp.add_handler
    function(CMH('start', public.start.init))
    function(CMH('rules', public.rules.init))
    function(CMH('source', public.source.init))
    function(MH(Filters.text("@admin"), public.report.init))

def admin_command(dsp):
    function = dsp.add_handler
    function(CMH('ban', admin.ban.init))
    function(CMH('status', admin.info_group.init))
    function(CMH('lang', admin.set_lang.init))
    function(CMH('mute', admin.mute.init))
    function(CMH('warn', admin.warn.init))
    function(CQH(admin.set_lang.language_en, pattern='language_en'))
    function(CQH(admin.set_lang.language_it, pattern='language_it'))

def owner_command(dsp):
    function = dsp.add_handler
    function(CMH('b', owner.broadcast.init, run_async=True))
    function(CMH('s', owner.superban.init, run_async=True))
    function(CMH('server', owner.server_info.init))
    function(CMH('test', owner.test.init))
    function(CMH('exit', owner.exit.init))