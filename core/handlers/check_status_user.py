from core import decorators
from core.database.repository.user import UserRepository
from core.database.repository.group import GroupRepository
from core.utilities.functions import user_object, chat_object, ban_user, kick_user
from core.utilities.message import message

#@decorators.public.init
def check_status(update,context):
    chat = chat_object(update)
    user = user_object(update)
    user_db = UserRepository().getById(user.id)
    get_group = GroupRepository().getById(chat.id)
    warn_count = user_db['warn_count'] if user_db is not None else 0
    max_warn = get_group['max_warn']

    if user.username is None or "":
        kick_user(update, context)
        msg = "#Automatic Handler\n<code>{}</code> set a username! You were kicked for safety!"
        message(update,context,msg.format(user.id))
    if user_db:
        username = "@"+user.username
        data = [(username,user.id)]
        UserRepository().update(data)
    if user_db is None or "":
        username = "@"+user.username
        default_warn = 0
        data = [(user.id,username,default_warn)]
        UserRepository().add(data)
    if warn_count == max_warn:
        ban_user(update,context)
        msg = "#Automatic Handler\n<code>{}</code> has reached the maximum number of warns"
        message(update,context,msg.format(user.id))