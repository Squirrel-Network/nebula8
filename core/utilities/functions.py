#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

import time
import datetime
import pandas
import matplotlib.pyplot as plt
from matplotlib import style
from config import Config
from core.database.repository.user import UserRepository
from core.database.repository.group import GroupRepository
from core.database.db_connect import SqlAlchemyConnection
from telegram import ChatPermissions
from languages.getLang import languages

################################
###     GENERAL FUNCTIONS    ###
################################

OFFSET = 127462 - ord('A')

COLORS = [
        '#0066cc',
        '#cc0000',
        '#009933',
        '#009999',
        '#cc0066',
        '#cc6600',
        '#cccc00',
        '#66cc00',
        '#66cccc',
        '#6666ff'
        ]

"""
Example to use:
flag('it')
flag('en')
"""
def flag(code):
    code = code.upper()
    return chr(ord(code[0]) + OFFSET) + chr(ord(code[1]) + OFFSET)


def check_user_permission(update,context):
    user_status = member_status_object(update,context)
    if user_status.status == 'creator' or user_status.status == 'administrator':
        return True
    else:
        return False

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


#Mute/Unmute User by telegram_id with Time
def mute_user_by_id_time(update, context, user, value, mute_time = 30):
    bot = context.bot
    chat = update.effective_chat.id
    if value == True:
        mute = bot.restrict_chat_member(chat,user,ChatPermissions(
            can_send_messages=False,
            can_send_media_messages=False,
            can_send_other_messages=False,
            can_add_web_page_previews=False),until_date=int(time.time()+mute_time)
            )
    else:
        mute = bot.restrict_chat_member(chat,user,ChatPermissions(
            can_send_messages=True,
            can_send_media_messages=True,
            can_send_other_messages=True,
            can_add_web_page_previews=True),until_date=int(time.time()+mute_time)
            )
    return mute

#Mute/Unmute User by Username with Time
def mute_user_by_username_time(update, context, username, value, mute_time = 3600):
    bot = context.bot
    chat = update.effective_chat.id
    user = UserRepository().getByUsername(username)
    if user is None:
        print('User not found')
    if value == True:
        mute = bot.restrict_chat_member(chat,user['tg_id'],ChatPermissions(
            can_send_messages=False,
            can_send_media_messages=False,
            can_send_other_messages=False,
            can_add_web_page_previews=False),until_date=int(time.time()+mute_time)
            )
    else:
        mute = bot.restrict_chat_member(chat,user['tg_id'],ChatPermissions(
            can_send_messages=True,
            can_send_media_messages=True,
            can_send_other_messages=True,
            can_add_web_page_previews=True),until_date=int(time.time()+mute_time)
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

##########################
###   GROUP FUNCTIONS  ###
##########################

#Perform an update of a boolean setting of the group on the database
def update_db_settings(update,record, options):
    chat = update.effective_message.chat_id
    if options == True:
        data = [(0,chat)]
        upd = GroupRepository().update_group_settings(record, data)
    else:
        data = [(1,chat)]
        upd = GroupRepository().update_group_settings(record, data)
    return upd

def get_owner_list() -> list:
    rows = UserRepository().getOwners()
    arr_owners = []
    for a in rows:
        owners = int(a['tg_id'])
        arr_owners.append(owners)
    return arr_owners

#@decorators.admin.user_admin
def close_menu(update, context):
    query = update.callback_query
    languages(update,context)
    if query.data == 'closeMenu':
        query.message.delete()

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

def upd_charts_DESC(update,context):
    chat = chat_object(update)

    db = SqlAlchemyConnection()
    engine = db.engine

    style.use('seaborn-pastel')

    # Read data from database
    df = pandas.read_sql("SELECT COUNT(*) AS message, u.tg_username as username, u.tg_id FROM nebula_updates nu INNER JOIN users u ON u.tg_id = nu.tg_user_id WHERE DATE BETWEEN DATE_SUB(NOW(), INTERVAL 30 DAY) AND NOW() AND nu.tg_group_id = %s GROUP BY nu.tg_user_id ORDER BY message DESC LIMIT 10" % chat.id, engine)
    #Reverse Dataframe
    df = df[::-1]
    df.plot(kind="barh", x="username", y="message",figsize=(18,10),grid=True,color=COLORS,title="Top 10 users with the most updates in the last 30 days in the group {}".format(chat.title))
    #Save Dataframe to Jpeg
    plt.savefig('/var/www/naos.hersel.it/charts/{}desc.jpg'.format(chat.id))

def upd_charts_ASC(update,context):
    chat = chat_object(update)

    db = SqlAlchemyConnection()
    engine = db.engine

    style.use('seaborn-pastel')

    # Read data from database
    df = pandas.read_sql("SELECT COUNT(*) AS message, u.tg_username as username, u.tg_id FROM nebula_updates nu INNER JOIN users u ON u.tg_id = nu.tg_user_id WHERE DATE BETWEEN DATE_SUB(NOW(), INTERVAL 30 DAY) AND NOW() AND nu.tg_group_id = %s GROUP BY nu.tg_user_id ORDER BY message ASC LIMIT 10" % chat.id, engine)
    #Reverse Dataframe
    df = df[::-1]
    df.plot(kind="barh", x="username", y="message",figsize=(18,10),grid=True,color=COLORS,title="The 10 worst users with the most updates in the last 30 days in the group {}".format(chat.title))
    #Save Dataframe to Jpeg
    plt.savefig('/var/www/naos.hersel.it/charts/{}asc.jpg'.format(chat.id))

#Function to save the group to the database
def save_group(update):
    chat = update.effective_message.chat_id
    chat_title = update.effective_chat.title
    record = GroupRepository.SET_GROUP_NAME
    group = GroupRepository().getById(chat)
    if group:
        data = [(chat_title, chat)]
        GroupRepository().update_group_settings(record, data)
    else:
        dictionary = {
            "id_group": chat,
            "group_name": chat_title,
            "welcome_text": Config.DEFAULT_WELCOME.format("{mention}","{chat}"),
            "welcome_buttons": '{"buttons": [{"id": 0,"title": "Bot Logs","url": "https://t.me/nebulalogs"}]}',
            "rules_text": Config.DEFAULT_RULES,
            "community": 0,
            "languages": Config.DEFAULT_LANGUAGE,
            "set_welcome": 1,
            "max_warn": 3,
            "set_silence": 0,
            "exe_filter": 0,
            "block_new_member": 0,
            "set_arabic_filter": 0,
            "set_cirillic_filter": 0,
            "set_chinese_filter": 0,
            "set_user_profile_picture": 0,
            "gif_filter": 0,
            "set_cas_ban": 1,
            "type_no_username": 1,
            "log_channel": Config.DEFAULT_LOG_CHANNEL,
            "group_photo": 'https://naos.hersel.it/group_photo/default.jpg',
            "total_users": 0,
            "zip_filter": 0,
            "targz_filter": 0,
            "jpg_filter": 0,
            "docx_filter": 0,
            "apk_filter": 0,
            "zoophile_filter": 1,
            "sender_chat_block": 1,
            "spoiler_block": 0,
            "set_no_vocal": 0,
            "set_antiflood": 1,
            "ban_message": '{mention} has been <b>banned</b> from: {chat}',
            "created_at": datetime.datetime.utcnow().isoformat(),
            "updated_at": datetime.datetime.utcnow().isoformat()
        }
        GroupRepository().add_with_dict(dictionary)


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

def chat_status_object(update,context):
    chat = chat_object(update)
    bot = context.bot
    get_chat = bot.getChat(chat_id=chat.id)
    return get_chat

def chat_status_object_by_id(context,chat):
    bot = context.bot
    get_chat = bot.getChat(chat_id=chat)
    return get_chat

def member_status_object(update,context):
    bot = context.bot
    chat = chat_object(update)
    user = user_object(update)
    get_member = bot.getChatMember(chat.id,user.id)
    return get_member

def reply_member_status_object(update,context):
    bot = context.bot
    chat = chat_object(update)
    user = user_reply_object(update)
    get_member = bot.getChatMember(chat.id,user.id)
    return get_member
