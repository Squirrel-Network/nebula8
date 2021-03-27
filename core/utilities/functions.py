#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

import time
from core.database.repository.user import UserRepository
from telegram import ChatPermissions

#######################
### USER FUNCTIONS ####
#######################

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

#Ban a user by Username
def ban_user_by_username(update, context, username):
    bot = context.bot
    chat = update.effective_chat.id
    user = UserRepository().getByUsername(username)
    ban = bot.kick_chat_member(chat, user['tg_id'])
    return ban

#Ban a user by telegram_id
def ban_user_by_id(update, context, id):
    bot = context.bot
    chat = update.effective_chat.id
    ban = bot.kick_chat_member(chat, id)
    return ban

#Kicks a user, not a ban
def kick_user(update,context):
    bot = context.bot
    chat = update.effective_chat.id
    kick_temp = bot.kick_chat_member(chat, update.message.from_user.id,until_date=int(time.time()+30))
    return kick_temp

#Mute/Unmute User
def mute_user(update, context, value):
    bot = context.bot
    chat = update.effective_chat.id
    user = update.message.from_user.id
    if value == True:
        mute = bot.restrict_chat_member(chat,user,ChatPermissions(
            can_send_messages=False,
            can_send_media_messages=False,
            can_send_other_messages=False,
            can_add_web_page_previews=False)
            )
    else:
        mute = bot.restrict_chat_member(chat,user,ChatPermissions(
            can_send_messages=True,
            can_send_media_messages=True,
            can_send_other_messages=True,
            can_add_web_page_previews=True)
            )
    return mute

#Mute/Unmute User in response
def mute_user_reply(update, context, value):
    bot = context.bot
    chat = update.effective_chat.id
    user = update.message.reply_to_message.from_user
    if value == True:
        mute = bot.restrict_chat_member(chat,user.id,ChatPermissions(
            can_send_messages=False,
            can_send_media_messages=False,
            can_send_other_messages=False,
            can_add_web_page_previews=False)
            )
    else:
        mute = bot.restrict_chat_member(chat,user.id,ChatPermissions(
            can_send_messages=True,
            can_send_media_messages=True,
            can_send_other_messages=True,
            can_add_web_page_previews=True)
            )
    return mute

#Mute/Unmute User by telegram_id
def mute_user_by_id(update, context, user, value):
    bot = context.bot
    chat = update.effective_chat.id
    if value == True:
        mute = bot.restrict_chat_member(chat,user,ChatPermissions(
            can_send_messages=False,
            can_send_media_messages=False,
            can_send_other_messages=False,
            can_add_web_page_previews=False)
            )
    else:
        mute = bot.restrict_chat_member(chat,user,ChatPermissions(
            can_send_messages=True,
            can_send_media_messages=True,
            can_send_other_messages=True,
            can_add_web_page_previews=True)
            )
    return mute

##########################
### MESSAGE FUNCTIONS  ###
##########################

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

################################
### OBJECT ENTITY DEFINITION ###
################################

def bot_object(update,context):
    bot = context.bot
    return bot

def chat_object(update):
    chat = update.effective_chat
    return chat

def user_object(update):
    user = update.effective_message.from_user
    return user

def user_reply_object(update):
    user = update.message.reply_to_message.from_user
    return user

def new_user_object(update):
    for member in update.message.new_chat_members:
        new_user = member
        return new_user