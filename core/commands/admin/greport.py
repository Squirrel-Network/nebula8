#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core import decorators
from languages.getLang import languages
from core.utilities.message import message
from core.utilities.functions import chat_object
from core.handlers.logs import staff_loggers

@decorators.public.init
@decorators.admin.user_admin
@decorators.delete.init
def init(update, context):
    bot = context.bot
    chat = chat_object(update)
    languages(update,context)
    if update.effective_message.reply_to_message:
        message(update, context, languages.delete_error_msg)
    else:
        link = bot.export_chat_invite_link(chat.id)
        msg = "#GlobalReport\nChatId: {}\nChat: {}\nLink: {}".format(chat.id, chat.title, link)
        msg_report = languages.global_report_msg
        staff_loggers(update, context, msg)
        message(update, context, msg_report)