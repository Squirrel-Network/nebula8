#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core.commands import public ,admin, owner
from telegram.ext import (CommandHandler as CMH,CallbackQueryHandler as CQH)

def user_command(dsp):
    function = dsp.add_handler
    ######################
    ### CommandHandler ###
    ######################
    function(CMH('start', public.start.init))
    function(CMH('help', public.help.init))
    function(CMH('rules', public.rules.init))
    function(CMH('io', public.io.init))
    function(CMH('source', public.source.init))
    function(CMH('report', public.report.global_report))

def admin_command(dsp):
    function = dsp.add_handler
    ######################
    ### CommandHandler ###
    ######################
    function(CMH('ban', admin.ban.init))
    function(CMH('status', admin.info_group.init))
    function(CMH('lang', admin.set_lang.init))
    function(CMH('mute', admin.mute.init))
    function(CMH('check', admin.check_permission.init))
    function(CMH('warn', admin.warn.init))
    function(CMH('info', admin.user_info.init))
    function(CMH('say', admin.say.init))
    function(CMH('welcome', admin.set_welcome.init))
    function(CMH('settings', admin.settings.init))
    function(CMH('delete', admin.delete_message.init))
    #############################
    ### CallbackQuery Handler ###
    #############################
    function(CQH(owner.superban.update_superban, pattern='m'))
    function(CQH(owner.superban.update_superban, pattern='closeMenu'))
    function(CQH(admin.mute.update_mute, pattern='unmute'))
    function(CQH(admin.set_lang.language_en, pattern='language_en'))
    function(CQH(admin.set_lang.language_it, pattern='language_it'))
    function(CQH(admin.settings.update_settings))

def owner_command(dsp):
    function = dsp.add_handler
    ######################
    ### CommandHandler ###
    ######################
    function(CMH('b', owner.broadcast.init, run_async=True))
    function(CMH('s', owner.superban.init, run_async=True))
    function(CMH('server', owner.server_info.init))
    function(CMH('community', owner.add_community.init))
    function(CMH('test', owner.test.init))
    function(CMH('exit', owner.exit.init))