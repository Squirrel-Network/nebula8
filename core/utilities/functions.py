#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

import time
from core.database.repository.user import UserRepository
from core.database.repository.group import GroupRepository
from core import decorators
from telegram import ChatPermissions
from languages.getLang import languages

#######################
# GENERAL FUNCTIONS ###
#######################

"""
Example:
flag('it')
flag('en')
"""
OFFSET = 127462 - ord('A')

def flag(code):
    code = code.upper()
    return chr(ord(code[0]) + OFFSET) + chr(ord(code[1]) + OFFSET)

#######################
### USER FUNCTIONS ####
#######################

#Ban a user
def ban_user(update,context):
    bot = context.bot
    chat = update.effective_chat.id
    user = update.message.from_user.id
    kick = bot.ban_chat_member(chat,user)
    return kick

#Ban a user in response
def ban_user_reply(update,context):
    bot = context.bot
    chat = update.effective_chat.id
    user = update.message.reply_to_message.from_user
    ban = bot.ban_chat_member(chat,user.id)
    return ban

#Ban a user by Username
def ban_user_by_username(update, context, username):
    bot = context.bot
    chat = update.effective_chat.id
    user = UserRepository().getByUsername(username)
    ban = bot.ban_chat_member(chat, user['tg_id'])
    return ban

#Ban a user by telegram_id
def ban_user_by_id(update, context, id):
    bot = context.bot
    chat = update.effective_chat.id
    ban = bot.ban_chat_member(chat, id)
    return ban

#Kicks a user, not a ban
def kick_user(update,context):
    bot = context.bot
    chat = update.effective_chat.id
    kick_temp = bot.ban_chat_member(chat, update.message.from_user.id,until_date=int(time.time()+30))
    return kick_temp

#Kicks a user, not a ban by Id
def kick_user_by_id(update,context,user):
    bot = context.bot
    chat = update.effective_chat.id
    kick_temp = bot.ban_chat_member(chat, user, until_date=int(time.time()+30))
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

#GET OWNERS LIST
def get_owner_list() -> list:
    rows = UserRepository().getOwners()
    arr_owners = []
    for a in rows:
        owners = int(a['tg_id'])
        arr_owners.append(owners)
    return arr_owners

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

##########################
###   GROUP FUNCTIONS  ###
##########################

def update_db_settings(update,record, options):
    chat = update.effective_message.chat_id
    if options == True:
        data = [(0,chat)]
        upd = GroupRepository().update_group_settings(record, data)
    else:
        data = [(1,chat)]
        upd = GroupRepository().update_group_settings(record, data)
    return upd

@decorators.admin.user_admin
def close_menu(update, context):
    query = update.callback_query
    languages(update,context)
    if query.data == 'closeMenu':
        query.edit_message_text(languages.close_menu_general, parse_mode='HTML')

def dynamic_perms(csm = True, csmm = True, csp = True, csom = True, cawpp = True, cci = False, ciu = False, cpm = False):
    return ChatPermissions(
        can_send_messages=csm,
        can_send_media_messages=csmm,
        can_send_polls=csp,
        can_send_other_messages=csom,
        can_add_web_page_previews=cawpp,
        can_change_info=cci,
        can_invite_users=ciu,
        can_pin_messages=cpm
        )

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