#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core import decorators
from core.utilities.message import message
from core.utilities.functions import chat_object,update_db_settings
from core.database.repository.group import GroupRepository
from core.utilities.constants import PERM_FALSE

@decorators.admin.user_admin
@decorators.delete.init
def init(update, context):
    bot = context.bot
    chat = chat_object(update)
    record_arabic = GroupRepository.SET_ARABIC
    record_chinese = GroupRepository.SET_CHINESE
    record_cirillic = GroupRepository.SET_CIRILLIC
    record_no_user_photo = GroupRepository.SET_USER_PROFILE_PICT
    record_silence = GroupRepository.SET_SILENCE


    data = [(0,1,chat.id)]
    GroupRepository().set_block_entry(data)
    update_db_settings(update, record_arabic, False)
    update_db_settings(update, record_chinese, False)
    update_db_settings(update, record_cirillic, False)
    update_db_settings(update, record_no_user_photo, False)
    update_db_settings(update, record_silence, False)

    bot.set_chat_permissions(update.effective_chat.id, PERM_FALSE)
    message(update, context, '<b>Attention! By activating this command you have completely blocked the group!!!\nto change the settings again you have to type /settings</b>')