from core import decorators
from core.utilities.functions import delete_message_reply
from core.utilities.message import message

@decorators.admin.user_admin
@decorators.delete.init
def init(update,context):
    reply = update.message.reply_to_message
    if reply is not None:
        delete_message_reply(update,context)
    else:
        message(update, context, "This command is used in response to a message!")