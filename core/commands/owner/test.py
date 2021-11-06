#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core import decorators
from core.utilities.functions import bot_object

@decorators.owner.init
def init(update,context):
     bot = bot_object(update,context)
     chat = update.effective_message.chat_id
     get_bot = bot.getChatMember(chat,bot.id)
     print(get_bot)