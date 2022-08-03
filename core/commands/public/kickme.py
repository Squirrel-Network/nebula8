#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core import decorators
from core.utilities.message import message
from core.utilities.functions import kick_user_by_id, user_object

@decorators.delete.init
def init(update,context):
    user = user_object(update)
    img = 'https://i.imgur.com/CKU9Y75.png'
    kick_user_by_id(update, context, user.id)
    message(update, context, 'You kicked yourself <code>[{}]</code>\nWe only used 15 lines of code to make a free feature, not paid\nPut a stars to our repository => /source'.format(user.id), 'HTML', 'photo', None, img)