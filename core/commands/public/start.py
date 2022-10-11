#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core import decorators
from languages.getLang import languages
from core.utilities.message import message
from core.utilities.functions import bot_object, user_object, chat_object
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.utilities.menu import build_menu

@decorators.private.init
@decorators.delete.init
def init(update, context):
    bot = context.bot
    languages(update,context)
    chat = update.effective_message.chat_id
    get_bot = bot_object(update,context)
    user = user_object(update)
    get_user_lang = user.language_code
    if get_user_lang == 'it':
        list_buttons = []
        list_buttons.append(InlineKeyboardButton('Commands', url='https://github.com/Squirrel-Network/nebula8/wiki/Command-List'))
        list_buttons.append(InlineKeyboardButton('Dashboard', url='https://nebula.squirrel-network.online'))
        list_buttons.append(InlineKeyboardButton('Api', url='https://api.nebula.squirrel-network.online'))
        list_buttons.append(InlineKeyboardButton('Knowhere', url='https://squirrel-network.online/knowhere'))
        list_buttons.append(InlineKeyboardButton('News', url='https://t.me/nebulanewsbot'))
        list_buttons.append(InlineKeyboardButton('Logs', url='https://t.me/nebulalogs'))
        list_buttons.append(InlineKeyboardButton('SquirrelNetwork', url='https://t.me/squirrelnetwork'))
        list_buttons.append(InlineKeyboardButton('👥 Add me to a Group', url='https://t.me/thenebulabot?startgroup=start'))
        menu = build_menu(list_buttons, 3)
        text = "🤖 Ciao io mi chiamo {}\n\nSono un bot ricco di funzionalità per la gestione dei gruppi\n"\
               "Possiedo una <b>Blacklist</b> enorme ho un antispam, un antiflood e molto altro ancora!!\n\n"\
               "ℹ Se hai bisogno di aiuto: [/help]\n\n\n🔵 Sapevi che sono OpenSource e cerco sempre aiuto? [/source]".format("@"+get_bot.username)
        bot.send_message(chat, text, reply_markup=InlineKeyboardMarkup(menu),parse_mode='HTML')
    else:
        message(update,context,languages.start.format("@"+get_bot.username))