#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core.database.repository.group import GroupRepository
from languages.getLang import languages
from core.utilities.message import message
from core.handlers.welcome import save_group
from core import decorators

@decorators.admin.user_admin
@decorators.bot.check_is_admin
@decorators.public.init
@decorators.bot.check_can_delete
@decorators.delete.init
def init(update, context):
    languages(update,context)
    chat = update.effective_message.chat_id
    chat_title = update.effective_chat.title
    record = GroupRepository.SET_GROUP_NAME
    row = GroupRepository().getById([chat])
    if row:
        data = [(chat_title, chat)]
        GroupRepository().update_group_settings(record, data)
        message(update,context,languages.group_info.format(
            row['group_name'],
            row['id_group'],
            row['welcome_text'],
            row['rules_text'],
            row['languages'],
            row['max_warn']))
    else:
        save_group(update)