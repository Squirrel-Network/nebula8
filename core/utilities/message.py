#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
import asyncio
import urllib.request
import requests
from config import Config

MAIN_URL = "https://api.telegram.org/"
TOKEN = Config.BOT_TOKEN

def message(update,context,text = ""):
    bot = context.bot
    chat = update.effective_chat.id
    msg = bot.send_message(chat,text,parse_mode='HTML')
    return msg

def messageMarkdown(update,context, text= ""):
    bot = context.bot
    chat = update.effective_chat.id
    msg = bot.send_message(chat,text,parse_mode='MarkdownV2')
    return msg

def messageWithId(update,context,chat,text = ""):
    bot = context.bot
    msg = bot.send_message(chat,text,parse_mode='HTML')
    return msg

def reply_message(update,context,text = ""):
    msg = update.message.reply_text(text,parse_mode='HTML')
    return msg

def PrivateMessage(update,context, text = ""):
    bot = context.bot
    msg = bot.send_message(update.message.from_user.id,text,parse_mode='HTML')
    return msg

def messagePhoto(update, context, img, desc = ''):
    bot = context.bot
    photo = bot.sendPhoto(chat_id=update.effective_chat.id, photo=img, caption=desc, parse_mode='HTML')
    return photo

def ApiMessage(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = MAIN_URL + "bot{}/sendmessage?chat_id={}&text={}&parse_mode=HTML".format(TOKEN, chat_id, text)
    send =  requests.get(url)
    return  send

async def messageWithAsync(update,context,delay,text = ""):
    bot = context.bot
    chat = update.effective_chat.id
    await asyncio.sleep(delay)
    msg = bot.send_message(chat,text,parse_mode='HTML')
    return msg

async def messageWithAsyncById(update,context,chat,delay,text = ""):
    bot = context.bot
    await asyncio.sleep(delay)
    msg = bot.send_message(chat,text,parse_mode='HTML')
    return msg