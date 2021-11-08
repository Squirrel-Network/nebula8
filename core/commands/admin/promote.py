#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from telegram.error import BadRequest
from core import decorators
from core.utilities.message import message
from core.utilities.functions import bot_object, chat_object, user_reply_object
from languages.getLang import languages

@decorators.admin.user_admin
def init(update,context):
    try:
        languages(update,context)
        if update.message.reply_to_message:
            bot = bot_object(update,context)
            chat = chat_object(update)
            user = user_reply_object(update)
            bot.promoteChatMember(chat.id,user.id,
            can_change_info=True,
            can_delete_messages=True,
            can_invite_users=True,
            can_restrict_members=True,
            can_pin_messages=True,
            can_promote_members=True
            )
        else:
            message(update,context,languages.delete_error_msg)
    except BadRequest:
        message(update,context,text="Non ho il permesso per promuovere questo utente come admin!\nPuoi darmi questo permesso spuntando il flag:\n <i>Aggiungere Amministratori</i>")