#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

import requests
from core import decorators
from bs4 import BeautifulSoup
from core.utilities.menu import build_menu
from core.utilities.message import message
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

@decorators.delete.init
def init(update, context):
    bot = context.bot
    r = requests.get("https://distrowatch.com/random.php")
    parsed_html = BeautifulSoup(r.text, features="html.parser")
    distro_long_name = parsed_html.title.string[17:].lower()
    distro_name = distro_long_name.split()[0]
    distro_url = f'https://distrowatch.com/table.php?distribution={distro_name}'
    distro_message = "Here is a random linux distribution: "
    button_list = [InlineKeyboardButton("🐧 ▶️ ", url=distro_url)]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
    bot.send_message(update.message.chat_id,text=distro_message,reply_markup=reply_markup,parse_mode='HTML')