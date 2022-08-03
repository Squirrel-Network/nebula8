#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core import decorators
from core.utilities.functions import chat_object
from core.utilities.message import message

@decorators.owner.init
@decorators.delete.init
def init(update, context):
    bot = context.bot
    chat = chat_object(update)
    link = bot.export_chat_invite_link(chat.id)
    message(update, context, "An invitation link was generated for the chat <b>{}</b>\nThe invitation was sent in <i>private</i>".format(chat.title))
    message(update, context, "Chat: {}\nInvite Link: {}".format(chat.title,link), 'HTML', 'private')

@decorators.owner.init
@decorators.delete.init
def manual_export(update,context):
    bot = context.bot
    chat = update.message.text[8:].strip()
    print(chat)
    link = bot.export_chat_invite_link(chat)
    message(update, context, "Invite Link: {}".format(link), 'HTML', 'private')