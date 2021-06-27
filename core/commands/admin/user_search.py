#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core import decorators
from core.utilities.functions import user_reply_object
from core.utilities.message import message
from core.database.repository.user import UserRepository

@decorators.admin.user_admin
def init(update,context):
    text = update.message.text
    if update.message.reply_to_message:
        user = user_reply_object(update)
        row = UserRepository().getById(user.id)
        if row:
            message(update, context, text="<b>The user search returned the following results:</b>\nTelegram Id: <code>{}</code>\nUsername: {}\nLast Update: {}"
            .format(
                row['tg_id'],
                row['tg_username'],
                row['updated_at'].isoformat()
                ))
        else:
            message(update,context, text="The user is not present in the database")
    else:
        input_user_id = text[8:].strip().split(" ", 1)
        user_id = input_user_id[0]
        if user_id != "":
            row = UserRepository().getById(int(user_id))
            if row:
                message(update, context, text="<b>The user search returned the following results:</b>\nTelegram Id: <code>{}</code>\nUsername: {}\nLast Update: {}"
                .format(
                    row['tg_id'],
                    row['tg_username'],
                    row['updated_at'].isoformat()
                    ))
            else:
                message(update,context, text="The user is not present in the database")
        else:
            message(update,context,"Attention the user id you entered does not exist!")