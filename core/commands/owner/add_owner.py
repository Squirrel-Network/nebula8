#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core import decorators
from core.utilities.functions import user_reply_object
from core.database.repository.user import UserRepository
from core.utilities.message import message

@decorators.owner.init
@decorators.delete.init
def init(update,context):
    if update.message.reply_to_message:
        user = user_reply_object(update)
        user_id = user.id
        row = UserRepository().getOwnerById(user.id)
        if row:
            message(update,context, "This owner already exists in the database")
        else:
            username = "@"+user.username
            data = [(user_id, username)]
            UserRepository().add_owner(data)
            message(update,context, "You have entered a new owner in the database!")
            
    else:
        message(update,context, "Error! This command should be used in response to the user!")