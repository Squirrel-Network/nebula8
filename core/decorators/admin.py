import os
from config import Config
from functools import wraps
from telegram import Chat, ChatMember

DEL_CMDS = bool(os.environ.get("DEL_CMDS", False))
LIST_OF_ADMINS = Config.SUPERADMIN

#New Function
def is_user_admin(chat: Chat, user_id: int, member: ChatMember = None) -> bool:
    if chat.type == 'private' \
            or user_id in LIST_OF_ADMINS \
            or chat.all_members_are_administrators:
        return True

    if not member:
        member = chat.get_member(user_id)
    return member.status in ('administrator', 'creator')

def user_admin(func):
    @wraps(func)
    def is_admin(update, context, *args, **kwargs):
        user = update.effective_user
        if user and is_user_admin(update.effective_chat, user.id):
            return func(update, context, *args, **kwargs)

        elif not user:
            pass

        elif DEL_CMDS and " " not in update.effective_message.text:
            update.effective_message.delete()

        else:
            update.effective_message.reply_text("Non sei un amministratore!")

    return is_admin