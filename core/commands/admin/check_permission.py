from core import decorators
from core.utilities.functions import bot_object
from core.utilities.message import message

@decorators.admin.user_admin
@decorators.public.init
def init(update, context):
    bot = bot_object(update, context)
    chat_id = update.message.chat_id
    get_bot = bot.getChatMember(chat_id,bot.id)

    perm_delete = get_bot.can_delete_messages
    perm_ban = get_bot.can_restrict_members
    perm_pin = get_bot.can_pin_messages
    perm_edit_msg = get_bot.can_be_edited
    if None in [perm_delete, perm_ban, perm_pin, perm_edit_msg]:
        message(update,context, "The bot does not have the correct permissions to function properly!❌\nPlease promote the bot as an admin")
    else:
        message(update, context, "The bot has the correct permissions to function properly ✅")