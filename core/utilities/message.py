#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
import asyncio

def message(update,context,text = ""):
    bot = context.bot
    chat = update.effective_chat.id
    msg = bot.send_message(chat,text,parse_mode='HTML')
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

async def messageWithAsync(update,context,delay,text = ""):
    bot = context.bot
    chat = update.effective_chat.id
    await asyncio.sleep(delay)
    msg = bot.send_message(chat,text,parse_mode='HTML')
    return msg
    