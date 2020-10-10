from core.database.repository.get_superban import SuperbanRepository
from languages.getLang import languages
from core.utilities.message import message
from core.utilities.functions import kick_user
from core.utilities.functions import delete_message
from telegram.ext.dispatcher import run_async

@run_async
def init(update, context):
    ban_user = str(update.effective_user.id)
    rows = SuperbanRepository().getById([ban_user])
    if rows:
        msg = "text"
        message(update,context,msg)
        delete_message(update,context)
        kick_user(update,context)