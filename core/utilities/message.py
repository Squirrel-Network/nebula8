#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
import asyncio
import urllib.request
import requests
from config import Config

MAIN_URL = "https://api.telegram.org/"
TOKEN = Config.BOT_TOKEN

def TopicMessage(thread_id,chat_id,text = ""):
    url = MAIN_URL + "bot{}/sendmessage?message_thread_id={}&chat_id={}&text={}&parse_mode=HTML".format(TOKEN, thread_id,chat_id, text)
    send = requests.get(url)
    return send
def message(update, context, text = "", parse = 'HTML', type = 'message', chatid=None, img=None, reply_markup = None):
    bot = context.bot
    chat = update.effective_chat.id
    thread_id = update.effective_message.message_thread_id

    if type == 'message':
        send = bot.send_message(chat, text, parse_mode=parse,message_thread_id=thread_id,reply_markup=reply_markup)
    elif type == 'photo':
        send = bot.sendPhoto(chat_id=update.effective_chat.id, photo=img, caption=text, parse_mode=parse,message_thread_id=thread_id)
    elif type == 'reply':
        send = update.message.reply_text(text, parse_mode=parse,message_thread_id=thread_id,reply_markup=reply_markup)
    elif type == 'messageid':
        send = bot.send_message(chatid,text,parse_mode=parse)
    elif type == 'private':
        send = bot.send_message(update.message.from_user.id,text,parse_mode=parse,reply_markup=reply_markup)
    elif type == 'animation':
        send = bot.sendAnimation(chat, img, caption=text,message_thread_id=thread_id)
    return send

def ApiMessage(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = MAIN_URL + "bot{}/sendmessage?chat_id={}&text={}&parse_mode=HTML".format(TOKEN, chat_id, text)
    send =  requests.get(url)
    return  send

def ApiGroupRemove(chat_id):
    url = MAIN_URL + "bot{}/leaveChat?chat_id={}".format(TOKEN,chat_id)
    send = requests.get(url)
    return send

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