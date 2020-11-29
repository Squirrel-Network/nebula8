from core.utilities.message import message
from core import decorators
from core.utilities.functions import chat_object

@decorators.owner.init
def init(update,context):
    var = chat_object(update)
    print(var)
    print(update.message.migrate_to_chat_id)
    #message(update,context,var)