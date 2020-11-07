from core import decorators
from core.utilities.message import message

@decorators.owner.init
def init(update, context):
    text = "BROADCAST"
    message(update,context,text)