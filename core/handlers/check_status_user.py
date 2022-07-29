#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
import datetime
from core import decorators
from core.utilities.constants import *
from core.utilities.message import message
from core.database.repository.user import UserRepository
from core.handlers.flood_wait import Flood_Manager_Python
from core.database.repository.group import GroupRepository
from core.database.repository.superban import SuperbanRepository
from core.database.repository.dashboard import DashboardRepository
from core.utilities.functions import user_object, chat_object, ban_user, kick_user, delete_message, mute_user_by_id, member_status_object, chat_status_object, check_user_permission

flood_manager = Flood_Manager_Python()

@decorators.public.init
def check_status(update,context):
    # Telegram Variables
    bot = context.bot
    chat = chat_object(update)
    user = user_object(update)
    get_superban_user_id = update.effective_user.id
    user_photo = user.get_profile_photos(user.id)
    user_status = member_status_object(update,context)
    chat_status = chat_status_object(update, context)

    #Get Group via Database
    get_group = GroupRepository().getById(chat.id)
    #Get User via Database
    user_db = UserRepository().getById(user.id)
    #Get User via Database in Many to Many Association
    get_user = UserRepository().getUserByGroup([user.id,chat.id])
    #Get User in Superban Table
    get_superban = SuperbanRepository().getById(get_superban_user_id)
    #get user in Dashboard
    get_dashboard = DashboardRepository().getById(user.id)
    #Get User Warn
    warn_count = get_user['warn_count'] if get_user is not None else DEFAULT_COUNT_WARN
    #Get Max Warn in group
    max_warn = get_group['max_warn'] if get_group is not None else DEFAULT_MAX_WARN

    if get_group:
        user_set_photo = get_group['set_user_profile_picture']
        type_no_username = get_group['type_no_username']
    else:
        user_set_photo = 0
    #Check if the user has a username if he does not have a username I perform a temporary kick and check that the user is not a service account
    if update.effective_user.id == SERVICE_ACCOUNT:
        print("Service Account")
    elif user.username is None or user.username == "":
        if type_no_username == 1:
            kick_user(update, context)
            msg = "#Automatic Handler\n<code>{}</code> set an username! You were kicked for safety!"
            message(update,context,msg.format(user.id))
        elif type_no_username == 2:
            msg = "#Automatic Handler\n<code>{}</code> set an username!"
            message(update,context,msg.format(user.id))
        elif type_no_username == 3:
            mute_user_by_id(update, context, user.id, True)
            msg = "#Automatic Handler\n<code>{}</code> set an username! You were Muted for safety!"
            message(update,context,msg.format(user.id))
        elif type_no_username == 4:
            ban_user(update,context)
            msg = "#Automatic Handler\n<code>{}</code> was banned because they didn't have an username"
            message(update,context,msg.format(user.id))
        elif type_no_username == 5:
            kick_user(update, context)
        else:
            print("No action even if you don't have a username")
    else:
        #Check if the user exists on the database if it exists makes an update of his username and his latest update if not exist insert it
        if user_db:
            #Get the Current Time
            current_time = datetime.datetime.utcnow().isoformat()
            username = "@"+user.username
            data = [(username,current_time,user.id)]
            UserRepository().update(data)
            data_mtm = [(user.id, chat.id, DEFAULT_COUNT_WARN,DEFAULT_USER_SCORE)]
            UserRepository().add_into_mtm(data_mtm)
        else:
            #Get the Current Time
            current_time = datetime.datetime.utcnow().isoformat()
            username = "@"+user.username
            data = [(user.id,username,current_time,current_time)]
            UserRepository().add(data)
            data_mtm = [(user.id, chat.id, DEFAULT_COUNT_WARN,DEFAULT_USER_SCORE)]
            UserRepository().add_into_mtm(data_mtm)
    #Check if the user has a profile photo
    if user_photo.total_count == 0 and user_set_photo == 1:
        kick_user(update, context)
        msg = "#Automatic Handler\n<code>{}</code> set a profile picture! You were kicked for safety!"
        message(update,context,msg.format(user.id))
    #Check if the user has been blacklisted
    if get_superban:
        superban_reason = get_superban['motivation_text']
        msg = '#Automatic Handler\nI got super banned <a href="tg://user?id={}">{}</a> <code>[{}]</code>\nFor the following Reason: {}'.format(user.id,user.first_name,user.id,superban_reason)
        message(update,context,msg)
        delete_message(update,context)
        ban_user(update,context)
    #If a user is enabled on the dashboard, I perform an update
    if get_dashboard:
        username = "@"+user.username
        save_date = datetime.datetime.utcnow().isoformat()
        dash_data = [(username, user_status.status, save_date, user.id, chat_status.id)]
        DashboardRepository().update(dash_data)
    #Check if the user has reached the maximum number of warns and ban him
    if warn_count == max_warn and check_user_permission(update,context) == False:
        ban_user(update,context)
        msg = "#Automatic Handler\n<code>{}</code> has reached the maximum number of warns"
        message(update,context,msg.format(user.id))
    #I run an antiflood check if a user exceeds the allowed limit the antiflood starts working
    if flood_manager.check_flood_wait(update) == 1 and get_group['set_antiflood'] == 1 and check_user_permission(update,context) == False:
        bot.delete_message(update.effective_message.chat_id, update.message.message_id)
        kick_user(update, context)
        msg = "#Automatic Handler\n<code>{}</code> has been kicked for flood".format(user.id)
        message(update,context,msg.format(user.id))