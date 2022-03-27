#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
import re
import datetime
from config import Config
from core import decorators
from core.utilities.menu import build_menu
from core.utilities.message import message, messageWithId
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.database.repository.superban import SuperbanRepository
from core.handlers.logs import sys_loggers, debug_channel
from core.utilities.strings import Strings
from core.utilities.regex import Regex

@decorators.owner.init
@decorators.delete.init
def init(update, context):
    #Variables
    text = update.message.text
    operator_id = update.message.from_user.id
    operator_username = "@"+update.message.from_user.username
    save_date = datetime.datetime.utcnow().isoformat()
    #Build a Keyboard Buttons
    buttons = []
    buttons.append(InlineKeyboardButton('Spam', callback_data='mSpam'))
    buttons.append(InlineKeyboardButton('Scam', callback_data='mScam'))
    buttons.append(InlineKeyboardButton('Userbot', callback_data='mUserbot'))
    buttons.append(InlineKeyboardButton('Porn', callback_data='mPorn'))
    buttons.append(InlineKeyboardButton('Other', callback_data='mOther'))
    buttons.append(InlineKeyboardButton('Illegal Content', callback_data='mIllegal_Content'))
    buttons.append(InlineKeyboardButton('Remove Superban', callback_data='removeSuperban'))
    buttons.append(InlineKeyboardButton('Close', callback_data='closeMenu'))
    menu = build_menu(buttons,2)
    if update.message.reply_to_message:
        user_id = update.message.reply_to_message.from_user.id
        update.message.reply_to_message.reply_text("Select a reason for the Superban", reply_markup=InlineKeyboardMarkup(menu))
    else:
        input_user_id = text[2:].strip().split(" ", 1)
        user_id = input_user_id[0]
        if user_id != "":
            number = re.search(Regex.HAS_NUMBER, user_id)
            if number is None:
                message(update,context,"Attention you must enter a number not letters!")
            else:
                default_motivation = "Other"
                data = [(user_id,default_motivation,save_date,operator_id)]
                SuperbanRepository().add(data)
                msg = 'You got super banned <a href="tg://user?id={}">{}</a>\nFor the following reason: <b>{}</b>\nGo to: https://squirrel-network.online/knowhere/?q={} to search for blacklisted users'.format(user_id,user_id,default_motivation,user_id)
                message(update,context,msg)
                logs_text = Strings.SUPERBAN_LOG.format(user_id,default_motivation,save_date,operator_username,operator_id)
                messageWithId(update,context,Config.DEFAULT_LOG_CHANNEL,logs_text)
                formatter = "Superban eseguito da: {}".format(operator_id)
                sys_loggers("[SUPERBAN_LOGS]",formatter,False,False,True)
                debug_channel(update, context, "[DEBUG_LOGGER] {}".format(formatter))
        else:
            message(update,context,"Attention you can not superbanned without entering an TELEGRAM ID!")

@decorators.owner.init
def multi_superban(update,context):
    txt = update.message.text
    x = re.findall(r'\d+', txt)
    string = "MultiSuperban eseguito! dei seguenti id:\n"
    for a in x:
        save_date = datetime.datetime.utcnow().isoformat()
        default_motivation = "MultiSuperban"
        operator_id = update.message.from_user.id
        data = [(a,default_motivation,save_date,operator_id)]
        SuperbanRepository().add(data)
        string += "▪️ {}\n".format(a)
    message(update,context,string)

@decorators.owner.init
def update_superban(update, context):
    bot = context.bot
    query = update.callback_query
    save_date = datetime.datetime.utcnow().isoformat()
    if query.data.startswith("m"):
        #Variables
        chat_id = query.message.chat_id
        operator_id = query.from_user.id
        operator_username = "@"+query.from_user.username
        user_id = query.message.reply_to_message.from_user.id
        motivation = query.data[1:]
        row = SuperbanRepository().getById(user_id)
        whitelist = SuperbanRepository().getWhitelistById(user_id)
        if whitelist:
            text_w = "This user is whitelisted you cannot blacklist!"
            query.edit_message_text(text_w, parse_mode='HTML')
        elif row:
            text = "Attention already superbanned user!"
            query.edit_message_text(text, parse_mode='HTML')
        else:
            data = [(user_id,motivation,save_date,operator_id)]
            SuperbanRepository().add(data)
            #Ban the User
            bot.ban_chat_member(chat_id, user_id)
            #Edit Message Text after push the button
            msg = 'You got super banned <a href="tg://user?id={}">{}</a>\nFor the following reason: <b>{}</b>\nGo to: https://squirrel-network.online/knowhere?q={} to search for blacklisted users'.format(user_id,user_id,motivation,user_id)
            query.edit_message_text(msg, parse_mode='HTML')
            #Telegram Logs
            logs_text = Strings.SUPERBAN_LOG.format(user_id,motivation,save_date,operator_username,operator_id)
            messageWithId(update,context,Config.DEFAULT_LOG_CHANNEL,logs_text)
            #System Logs
            formatter = "Superban eseguito da: {}".format(operator_id)
            sys_loggers("[SUPERBAN_LOGS]",formatter,False,False,True)
            debug_channel(update, context, "[DEBUG_LOGGER] {}".format(formatter))

    if query.data == "removeSuperban":
        user_id = query.message.reply_to_message.from_user.id
        row = SuperbanRepository().getById(user_id)
        if row:
            data = [(user_id)]
            SuperbanRepository().remove(data)
            msg = "I removed the superban to user <code>{}</code>".format(user_id)
            query.edit_message_text(msg,parse_mode='HTML')
        else:
            query.edit_message_text("Attention this user not super banned!!!",parse_mode='HTML')
    if query.data == 'closeMenu':
        query.edit_message_text("You have closed the Menu", parse_mode='HTML')