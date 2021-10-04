#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

import datetime
from core import decorators
from core.utilities.functions import chat_object
from core.database.repository.group import GroupRepository

@decorators.owner.init
def init(update,context):
      chat = chat_object(update)
      row = GroupRepository().getUpdatesByChat(chat.id)
      print(row)