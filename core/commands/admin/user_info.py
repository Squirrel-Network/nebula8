#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
import datetime
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
    user_db = UserRepository().getById(user.id)
    get_warn = UserRepository().getUserByGroup([user.id,chat.id])
    current_time = datetime.datetime.utcnow().isoformat()
    default_warn = 0
    if user_db:
        username = "@"+user.username
        data = [(username,current_time,user.id)]
        UserRepository().update(data)
        warn_count = get_warn['warn_count']
        data_mtm = [(user.id, chat.id, default_warn)]
        UserRepository().add_into_mtm(data_mtm)
        msg = Strings.USER_INFO.format(id=user.id,username=user.username,chat=chat.title,warn=warn_count)
        PrivateMessage(update,context,msg)
    else:
        username = "@"+user.username
        data = [(user.id,username,current_time,current_time)]
        UserRepository().add(data)
        data_mtm = [(user.id, chat.id, default_warn)]
        UserRepository().add_into_mtm(data_mtm)
        msg = Strings.USER_INFO.format(id=user.id,username=user.username,chat=chat.title,warn=default_warn)
        PrivateMessage(update,context,msg)