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
    function(MH(Filters.group, handlers.superban.init))
    function(CQH(handlers.welcome.select_language_en, pattern='select_language_en'))
    function(CQH(handlers.welcome.select_language_it, pattern='select_language_it'))