#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core import decorators
from core.database.repository.user import UserRepository
from core.database.repository.group import GroupRepository
from core.utilities.functions import user_reply_object, chat_object
from core.utilities.functions import ban_user_reply
from core.utilities.message import message

@decorators.admin.user_admin
@decorators.delete.init
def init(update,context):
    user = user_reply_object(update)
    chat = chat_object(update)
    get_user = UserRepository().getById(user.id)
    get_group = GroupRepository().getById(chat.id)

    warn_count = get_user['warn_count'] if get_user is not None else 0
    max_warn = get_group['max_warn']

    if warn_count != max_warn:
        if get_user:
            username = "@"+user.username
            data = [(username,user.id)]
            UserRepository().update(data)
            UserRepository().updateWarn([user.id])
            message(update,context,"{} was warned by the group {}".format(user.username,chat.title))
        else:
            username = "@"+user.username
            default_warn = 1
            data = [(user.id,username,default_warn)]
            UserRepository().add(data)
            message(update,context,"{} was warned by the group {}".format(user.username,chat.title))
    else:
        ban_user_reply(update,context)
        message(update,context,"User @{} has reached the maximum number\n of warns in the {} group and has been banned".format(user.username,chat.title))