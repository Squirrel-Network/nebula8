#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core import decorators
from core.database.repository.group import GroupRepository
from config import Config


@decorators.owner.init
def init(update,context):
        chat = update.effective_message.chat_id
        chat_title = update.effective_chat.title
        default_welcome = Config.DEFAULT_WELCOME.format("{username}","{chat}")
        default_buttons = '{"buttons": [{"id": 0,"title": "Bot Logs","url": "https://t.me/nebulalogs"}]}'
        default_rules = Config.DEFAULT_RULES
        default_lang = Config.DEFAULT_LANGUAGE
        default_community = 0
        default_set_welcome = 1
        default_max_warn = 3
        default_global_silence = 0
        default_exe_filter = 0
        default_block_user = 0
        default_arabic_filter = 1
        default_cirillic_filter = 1
        default_chinese_filter = 1
        default_user_profile_photo = 0
        default_gif_filter = 0
        default_set_cas_ban = 1
        default_type_no_username = 1
        default_log_channel = Config.DEFAULT_LOG_CHANNEL
        default_group_photo = 'https://naos.hersel.it/group_photo/default.jpg'
        default_count_group = 0

        data = (
            chat,
            chat_title,
            default_welcome,
            default_buttons,
            default_rules,
            default_community,
            default_lang,
            default_set_welcome,
            default_max_warn,
            default_global_silence,
            default_exe_filter,
            default_block_user,
            default_arabic_filter,
            default_cirillic_filter,
            default_chinese_filter,
            default_user_profile_photo,
            default_gif_filter,
            default_set_cas_ban,
            default_type_no_username,
            default_log_channel,
            default_group_photo,
            default_count_group
            )

        GroupRepository().add_2(data)
