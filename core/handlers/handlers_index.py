from core import handlers
from telegram.ext import (
    CommandHandler as CMH,
    MessageHandler as MH,
    CallbackQueryHandler as CQH,
    ConversationHandler as CH,
    Filters)

def core_handlers(dsp):
    function = dsp.add_handler
    function(MH(Filters.status_update.new_chat_members, handlers.welcome.init))