#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core import decorators
from core.utilities.message import message
from core.database.repository.superban import SuperbanRepository
from core.utilities.functions import user_reply_object

@decorators.owner.init
@decorators.delete.init
def init(update,context):
    if update.message.reply_to_message:
        user = user_reply_object(update)
        row = SuperbanRepository().getWhitelistById(user.id)
        if row:
            message(update, context, "You have already whitelisted this user")
        else:
            user_username = "@"+user.username
            data = [(user.id, user_username)]
            SuperbanRepository().addWhitelist(data)
            message(update, context, "You have entered the user {} in the Whitelist".format(user_username))
    else:
        message(update, context, "This message can only be used in response to a user")