from core.utilities.message import message
from core import decorators
from core.utilities.functions import chat_object, user_reply_object
from core.database.repository.user import UserRepository

@decorators.owner.init
def init(update,context):
    user = user_reply_object(update)
    chat = chat_object(update)
    user_by_group = UserRepository().getUserByGroup([user.id,chat.id])
    print(user_by_group)