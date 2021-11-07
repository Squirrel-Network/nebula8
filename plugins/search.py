#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core.utilities.menu import build_menu
from core.utilities.message import message
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

"""
/mdn {terms}
"""
def mdn(update, context):
    bot = context.bot
    msg=str(update.message.text[4:]).strip()
    if msg != "":
        main_text = "Here are the results of your MDN search"
        gurl = "https://developer.mozilla.org/en-US/search?q={0}".format(msg.replace(' ','+'))
        button_list = [InlineKeyboardButton("🔎 Search", url=gurl)]
        reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
        bot.send_message(update.message.chat_id,text=main_text,reply_markup=reply_markup,parse_mode='HTML')
    else:
        message(update,context, text="You need to type a search criteria!\nHow to use the command: <code>/mdn text</code>")
"""
/google {terms}
"""
def google(update, context):
    bot = context.bot
    msg=str(update.message.text[7:]).strip()
    if msg != "":
        main_text = "Here are the results of your Google search"
        gurl = "https://www.google.com/search?&q={0}".format(msg.replace(' ','+'))
        button_list = [InlineKeyboardButton("🔎 Search", url=gurl)]
        reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
        bot.send_message(update.message.chat_id,text=main_text,reply_markup=reply_markup,parse_mode='HTML')
    else:
        message(update,context, text="You need to type a search criteria!\nHow to use the command: <code>/google text</code>")
"""
/ddg {terms}
"""
def duckduckgo(update, context):
    bot = context.bot
    msg=str(update.message.text[4:]).strip()
    if msg != "":
        main_text = "Here are the results of your DuckDuckGo search"
        gurl = "https://duckduckgo.com/?q={0}".format(msg.replace(' ','+'))
        button_list = [InlineKeyboardButton("🔎 Search", url=gurl)]
        reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
        bot.send_message(update.message.chat_id,text=main_text,reply_markup=reply_markup,parse_mode='HTML')
    else:
        message(update,context, text="You need to type a search criteria!\nHow to use the command: <code>/ddg text</code>")