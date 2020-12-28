#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core import decorators
from core.utilities.message import PrivateMessage
from core.utilities.functions import user_reply_object, chat_object
from core.database.repository.user import UserRepository
from core.utilities.strings import Strings

@decorators.admin.user_admin
@decorators.delete.init
def init(update, context):
    user = user_reply_object(update)
    chat = chat_object(update)
    row = UserRepository().getById(user.id)
    if row:
        username = "@"+user.username
        data = [(username,user.id)]
        UserRepository().update(data)
        warn_count = row['warn_count']
        msg = Strings.USER_INFO.format(id=user.id,username=user.username,chat=chat.title,warn=warn_count)
        PrivateMessage(update,context,msg)
    else:
        username = "@"+user.username
        default_warn = 0
        data = [(user.id,username,default_warn)]
        UserRepository().add(data)
        msg = Strings.USER_INFO.format(id=user.id,username=user.username,chat=chat.title,warn=default_warn)
        PrivateMessage(update,context,msg)