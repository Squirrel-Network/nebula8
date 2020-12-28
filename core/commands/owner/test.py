from core.utilities.message import message
from core import decorators
from core.utilities.functions import chat_object

@decorators.owner.init
def init(update,context):
    msg = update.message.text
    x = msg.count(msg)
    print(x)