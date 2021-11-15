#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core import decorators
from core.utilities.message import message

@decorators.public.init
@decorators.delete.init
def init(update,context):
     administrators = update.effective_chat.get_administrators()
     string = ""
     for admin in administrators:
          user = admin.user
          string += '👮 <a href="tg://user?id={}">{}</a>\n\n'.format(user.id,user.first_name)
     message(update,context,"<b>Admin List:</b>\n{}".format(string))