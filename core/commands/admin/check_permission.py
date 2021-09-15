from core import decorators
from core.utilities.functions import bot_object
from core.utilities.message import message
from languages.getLang import languages

@decorators.admin.user_admin
@decorators.public.init
def init(update, context):
    bot = bot_object(update, context)
    chat_id = update.message.chat_id
    get_bot = bot.getChatMember(chat_id,bot.id)
    languages(update,context)

    perm_delete = get_bot.can_delete_messages
    perm_ban = get_bot.can_restrict_members
    perm_pin = get_bot.can_pin_messages
    perm_edit_msg = get_bot.can_be_edited
    perm_media = get_bot.can_send_media_messages
    perm_send_message = get_bot.can_send_messages
    if None in [perm_delete, perm_ban, perm_pin, perm_edit_msg, perm_media, perm_send_message]:
        message(update,context, languages.perm_error)
    else:
        message(update, context, languages.perm_ok)