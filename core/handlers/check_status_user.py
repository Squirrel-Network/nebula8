from core import decorators
from core.database.repository.user import UserRepository
from core.database.repository.group import GroupRepository
from core.database.repository.superban import SuperbanRepository
from core.utilities.functions import user_object, chat_object, ban_user, kick_user, delete_message
from core.utilities.message import message

@decorators.public.init
def check_status(update,context):
    chat = chat_object(update)
    user = user_object(update)
    get_superban_user_id = update.effective_user.id
    user_db = UserRepository().getById(user.id)
    get_superban = SuperbanRepository().getById(get_superban_user_id)
    default_count_warn = 0
    get_group = GroupRepository().getById(chat.id)
    user_photo = user.get_profile_photos(user.id)
    if get_group:
        user_set_photo = get_group['set_user_profile_picture']
    else:
        user_set_photo = 0
    #warn_count = user_db['warn_count'] if user_db is not None else 0
    #max_warn = get_group['max_warn']
    #if warn_count == max_warn:
        #ban_user(update,context)
        #msg = "#Automatic Handler\n<code>{}</code> has reached the maximum number of warns"
        #message(update,context,msg.format(user.id))

    if user.username is None or "":
        kick_user(update, context)
        msg = "#Automatic Handler\n<code>{}</code> set a username! You were kicked for safety!"
        message(update,context,msg.format(user.id))
    if user_photo.total_count == 0 and user_set_photo == 1:
        kick_user(update, context)
        msg = "#Automatic Handler\n<code>{}</code> set a profile picture! You were kicked for safety!"
        message(update,context,msg.format(user.id))
    if user_db:
        username = "@"+user.username
        data = [(username,user.id)]
        UserRepository().update(data)
        data_mtm = [(user.id, chat.id, default_count_warn)]
        UserRepository().add_into_mtm(data_mtm)
    if user_db is None or "":
        username = "@"+user.username
        default_warn = 0
        data = [(user.id,username,default_warn)]
        UserRepository().add(data)
        data_mtm = [(user.id, chat.id, default_count_warn)]
        UserRepository().add_into_mtm(data_mtm)
    if get_superban:
        msg = 'I got super banned <a href="tg://user?id={}">{}</a>'.format(user.id,user.first_name)
        message(update,context,msg)
        delete_message(update,context)
        ban_user(update,context)