from core.database.repository.group import GroupRepository
from core import decorators
from telegram import Update, ParseMode
from telegram.ext import CallbackContext

@decorators.owner.init
def init(update: Update, context: CallbackContext) -> None:
    context.bot.wrong_method_name()