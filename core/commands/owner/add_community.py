from core import decorators
from core.utilities.message import message
from core.utilities.functions import chat_object
from core.database.repository.community import CommunityRepository

@decorators.owner.init
def init(update,context):
    chat = chat_object(update)
    link = "https://t.me/{}".format(chat.username)
    row = CommunityRepository().getById(chat.id)
    if row:
        data = [(chat.title,chat.id)]
        CommunityRepository().update(data)
    else:
        data = [(chat.title,chat.id,link)]
        CommunityRepository().add(data)