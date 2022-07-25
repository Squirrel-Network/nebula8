#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core import decorators
from core.utilities.message import message
from core.database.repository.group import GroupRepository

@decorators.owner.init
@decorators.delete.init
def init(update,context):
    msg = update.message.text[5:].strip()
    if msg != "":
        GroupRepository().insert_spam(msg)
        message(update,context,"You have entered a new ANTISPAM logic in the database, the logic you have entered is the following: {}".format(msg))
    else:
        message(update, context,"Empty Logic")