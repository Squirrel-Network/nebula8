#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

import time

#Ban a user
def ban_user(update,context):
    bot = context.bot
    chat = update.effective_chat.id
    user = update.message.from_user.id
    kick = bot.kick_chat_member(chat,user)
    return kick

#Ban a user in response
def ban_user_reply(update,context):
    bot = context.bot
    chat = update.effective_chat.id
    user = update.message.reply_to_message.from_user
    ban = bot.kick_chat_member(chat,user.id)
    return ban

#Kicks a user, not a ban
def kick_user(update,context):
    bot = context.bot
    chat = update.effective_chat.id
    kick_temp = bot.kick_chat_member(chat, update.message.from_user.id,until_date=int(time.time()+30))
    return kick_temp

#Delete a message
def delete_message(update, context):
    bot = context.bot
    chat = update.effective_chat.id
    id_message = update.message.message_id
    delete = bot.delete_message(chat,id_message)
    return delete

#Delete a reply message
def delete_message_reply(update,context):
    bot = context.bot
    chat = update.effective_chat.id
    delete = bot.delete_message(chat, update.message.reply_to_message.message_id)
    return delete

##############################
###Object entity definition###
##############################
def bot_object(update,context):
    bot = context.bot
    return bot

def chat_object(update):
    chat = update.effective_chat
    return chat

def user_object(update):
    user = update.message.from_user
    return user

def new_user_object(update):
    for member in update.message.new_chat_members:
        new_user = member
        return new_user