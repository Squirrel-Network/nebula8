#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
import requests
from core import decorators
from languages.getLang import languages
from core.database.repository.group import GroupRepository

@decorators.delete.init
def init(update, context):
    bot = context.bot
    languages(update,context)
    api_meme = "https://memes.blademaker.tv/api?lang={}".format(languages.lang_default)
    get = requests.get(api_meme)
    response = get.json()
    img = response["image"]
    bot.sendPhoto(chat_id=update.effective_chat.id, photo=img, caption="Want another one? click /meme")