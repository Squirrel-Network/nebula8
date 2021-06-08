#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
import datetime
import requests
from core import decorators
from core.database.repository.user import UserRepository
from core.database.repository.group import GroupRepository
from core.database.repository.superban import SuperbanRepository
from core.utilities.functions import user_object, chat_object, ban_user, kick_user, delete_message
from core.utilities.message import message

#Constants
API_CAS = 'https://api.cas.chat/check?user_id={}'
DEFAULT_COUNT_WARN = 0

@decorators.public.init
def check_status(update,context):
    # Telegram Variables
    chat = chat_object(update)
    user = user_object(update)
    get_superban_user_id = update.effective_user.id
    user_photo = user.get_profile_photos(user.id)

    #Get Group via Database
    get_group = GroupRepository().getById(chat.id)
    #Get User via Database
    user_db = UserRepository().getById(user.id)
    #Get User via Database in Many to Many Association
    get_user = UserRepository().getUserByGroup([user.id,chat.id])
    #Get User in Superban Table
    get_superban = SuperbanRepository().getById(get_superban_user_id)
    #Get User Warn
    warn_count = get_user['warn_count'] if get_user is not None else 0
    #Get Max Warn in group
    max_warn = get_group['max_warn'] if get_group is not None else 3
    #Get the Current Time
    current_time = datetime.datetime.utcnow().isoformat()

    #CAS BAN Variables
    api_cas =  requests.get(API_CAS.format(get_superban_user_id))
    response = api_cas.json()
    cas_ban = response["ok"]

    if get_group:
        user_set_photo = get_group['set_user_profile_picture']
        cas_ban_row = get_group['set_cas_ban']
    else:
        user_set_photo = 0
        cas_ban_row = 1

    if user.username is None or "":
        kick_user(update, context)
        msg = "#Automatic Handler\n<code>{}</code> set a username! You were kicked for safety!"
        message(update,context,msg.format(user.id))
    if user_photo.total_count == 0 and user_set_photo == 1:
        kick_user(update, context)
        msg = "#Automatic Handler\n<code>{}</code> set a profile picture! You were kicked for safety!"
        message(update,context,msg.format(user.id))
    if user_db:
        username = "@"+user.username
        data = [(username,current_time,user.id)]
        UserRepository().update(data)
        data_mtm = [(user.id, chat.id, DEFAULT_COUNT_WARN)]
        UserRepository().add_into_mtm(data_mtm)
    if user_db is None or "":
        username = "@"+user.username
        data = [(user.id,username,current_time,current_time)]
        UserRepository().add(data)
        data_mtm = [(user.id, chat.id, DEFAULT_COUNT_WARN)]
        UserRepository().add_into_mtm(data_mtm)
    if get_superban:
        msg = '#Automatic Handler\nI got super banned <a href="tg://user?id={}">{}</a>'.format(user.id,user.first_name)
        message(update,context,msg)
        delete_message(update,context)
        ban_user(update,context)
    if warn_count == max_warn:
        ban_user(update,context)
        msg = "#Automatic Handler\n<code>{}</code> has reached the maximum number of warns"
        message(update,context,msg.format(user.id))
    if cas_ban == True and cas_ban_row == 1:
        result = response["result"]
        messages = result["messages"]
        date = result["time_added"]
        message(update,context,"#Automatic Handler\n<b>{}</b> is present into CAS's blacklist\nfor the following reason: <code>{}</code>\nin data: <b>{}</b>\n\nhttps://cas.chat/query?u={}".format(get_superban_user_id,messages,date,get_superban_user_id))