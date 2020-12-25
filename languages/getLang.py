#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from config import Config
from core.database.repository.group_language import GroupLanguageRepository
from languages import (EN,IT)

def get(update, context):
    chat = update.effective_message.chat_id
    row = GroupLanguageRepository().getById([chat])
    if row is None:
        return None
    else:
        return row['languages']

def languages(update,context):
    LANGUAGE = get(update,context)

    if LANGUAGE == "" or LANGUAGE is None:
        LANGUAGE = Config.DEFAULT_LANGUAGE

    if LANGUAGE == "IT":
        setLang = IT.Italian
    elif LANGUAGE == "EN":
        setLang = EN.English

    languages.start = setLang["START_COMMAND"]
    languages.helps = setLang["HELP_COMMAND"]
    languages.group_info = setLang["GROUP_INFO"]
    languages.bot_welcome = setLang["BOT_WELCOME"]
    languages.ban_message = setLang["BAN_MESSAGE"]
    languages.rules = setLang["RULES"]
    languages.user_ban = setLang["BAN_USER"]
    languages.bot_ban = setLang["BAN_BOT"]
    languages.ban_error = setLang["BAN_ERROR"]
    languages.ban_user_error = setLang["BAN_USER_ERROR"]
    languages.say_error = setLang["SAY_MESSAGE"]
    return LANGUAGE