#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
import requests
from core import decorators

@decorators.delete.init
def init(update,context):
    bot = context.bot
    url = r"http://inspirobot.me/api?generate=true"
    get = requests.get(url)
    img = get.text
    bot.sendPhoto(chat_id=update.effective_chat.id, photo=img)