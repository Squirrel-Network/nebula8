from core.utilities.message import message
from core import decorators

@decorators.owner.init
def init(update,context):
    message(update,context,"test")