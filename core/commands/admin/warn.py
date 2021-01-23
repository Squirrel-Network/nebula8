#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core import decorators
from core.database.repository.user import UserRepository
from core.database.repository.group import GroupRepository
from core.utilities.functions import user_reply_object, chat_object
from core.utilities.functions import ban_user_reply
from core.utilities.message import message
from core.handlers.logs import telegram_loggers

@decorators.admin.user_admin
@decorators.delete.init
def init(update,context):
    user = user_reply_object(update)
    chat = chat_object(update)
    get_user = UserRepository().getUserByGroup([user.id,chat.id])
    get_group = GroupRepository().getById(chat.id)
    warn_count = get_user['warn_count'] if get_user is not None else 0
    max_warn = get_group['max_warn']
    default_warn = 1

    if warn_count != max_warn:
        if get_user:
            default_warn_count = 0
            username = "@"+user.username
            data = [(username,user.id)]
            UserRepository().update(data)
            data_mtm = [(user.id, chat.id, default_warn_count)]
            UserRepository().add_into_mtm(data_mtm)
            data_warn = [(user.id,chat.id)]
            UserRepository().updateWarn(data_warn)
            message(update,context,"{} was warned by the group {}".format(username,chat.title))
            log_txt = "#Log {} was warned by the group {}".format(username,chat.title)
            telegram_loggers(update,context,log_txt)
        else:
            username = "@"+user.username
            data = [(user.id,username,default_warn)]
            UserRepository().add(data)
            data_mtm = [(user.id, chat.id, default_warn)]
            UserRepository().add_into_mtm(data_mtm)
            message(update,context,"{} was warned by the group {}".format(username,chat.title))
            log_txt = "#Log {} was warned by the group {}".format(username,chat.title)
            telegram_loggers(update,context,log_txt)
    else:
        ban_user_reply(update,context)
        message(update,context,"User @{} has reached the maximum number\n of warns in the {} group and has been banned".format(user.username,chat.title))