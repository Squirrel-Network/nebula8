from core import decorators
from core.utilities.message import message

def user_control(update,idutente = 0,username = ""):
    if username == "":
        print("EMPTY USERNAME!")
    elif idutente == 199:
        print("BLACKLISTED")
    else:
        user = update.message.reply_text("{username} add group".format(username=username))
        return user

@decorators.public.init
def init(update, context):
    for member in update.message.new_chat_members:
        user_control(update,member.id,member.username)