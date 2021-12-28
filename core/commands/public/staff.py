#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core import decorators
from telegram.utils.helpers import mention_markdown
from telegram.utils.helpers import escape_markdown


@decorators.public.init
@decorators.delete.init
def init(update,context):
     bot = context.bot
     administrators = update.effective_chat.get_administrators()
     chat = update.effective_chat.id
     string = "Group Staff:\n"
     for admin in administrators:
          user = admin.user
          user_first = user.first_name
          string += "👮 {}\n".format(mention_markdown(user.id, user_first, version=2))
     bot.send_message(chat,string,parse_mode='MarkdownV2')