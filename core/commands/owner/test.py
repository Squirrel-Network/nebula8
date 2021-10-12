#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core import decorators

@decorators.owner.init
def init(update,context):
      bot = context.bot
      bot.send_dice(chat_id=update.effective_chat.id, emoji="🎲")