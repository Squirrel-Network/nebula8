#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core import decorators
from core.utilities.message import message

@decorators.admin.user_admin
@decorators.delete.init
def init(update,context):
    msg = update.message.text[4:].strip()
    message(update,context,msg)