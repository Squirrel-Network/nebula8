import plugins
from telegram.ext import (
    CommandHandler as CMH,
    MessageHandler as MH,
    CallbackQueryHandler as CQH,
    ConversationHandler as CH)

def function_plugins(dsp):
    function = dsp.add_handler
    function(CMH('distro',plugins.distrowatch.init))