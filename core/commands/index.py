from core.commands import public ,admin, owner
from telegram.ext import (CommandHandler as CMH)

def user_command(dsp):
    function = dsp.add_handler
    function(CMH('start', public.start.init))

def admin_command(dsp):
    function = dsp.add_handler
    function(CMH('ban', admin.ban.init))
    function(CMH('status', admin.info_group.init))

def owner_command(dsp):
    function = dsp.add_handler
    function(CMH('b', owner.broadcast.init, run_async=True))
    function(CMH('server', owner.server_info.init))
    function(CMH('test', owner.test.init))
    function(CMH('exit', owner.exit.init))