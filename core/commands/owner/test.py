#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core import decorators
from core.database.repository.user import UserRepository

@decorators.owner.init
def init(update,context):
      bot = context.bot
      rows = UserRepository().getOwners()
      for a in rows:
            print(a['tg_id'])