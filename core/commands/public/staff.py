#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core import decorators
from core.utilities.message import message
from telegram.utils.helpers import mention_html

@decorators.public.init
@decorators.delete.init
def init(update,context):
     administrators = update.effective_chat.get_administrators()
     string = ""
     for admin in administrators:
          user = admin.user
          string += '👮 {}\n\n'.format(mention_html(user.id, user.first_name))
     message(update,context,"<b>Admin List:</b>\n{}".format(string))