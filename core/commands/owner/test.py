#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core import decorators
from core.utilities.message import ApiMessage

@decorators.owner.init
@decorators.delete.init
def init(update,context):
      text = update.message.text[5:].strip()
      chat = update.effective_chat.id
      ApiMessage(text, chat)