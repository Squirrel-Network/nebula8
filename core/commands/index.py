from core.commands import public ,admin, owner
from telegram.ext import (
    CommandHandler as CMH,
    MessageHandler as MH,
    CallbackQueryHandler as CQH,
    ConversationHandler as CH)

def user_command(dsp):
    function = dsp.add_handler
    function(CMH('start', public.start.init))
    #function(CQH(public.start.welcome_button, pattern='welcome_button'))
    #function(CQH(public.start.back_button, pattern='back_button'))

def admin_command(dsp):
    function = dsp.add_handler
    function(CMH('ban', admin.ban.init))
    function(CMH('status', admin.info_group.init))

def owner_command(dsp):
    function = dsp.add_handler
    function(CMH('test', owner.test.init))
    function(CMH('exit', owner.exit.init))