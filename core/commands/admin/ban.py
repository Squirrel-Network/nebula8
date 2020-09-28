from core import decorators
from core.utilities.message import message

@decorators.admin.user_admin
def init(update, context):
    text = "Ban"
    message(update,context,text)