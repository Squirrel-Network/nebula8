#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
import datetime
from config import Config
from core import decorators
from core.utilities.menu import build_menu
from core.utilities.message import message, messageWithId
from telegram.error import BadRequest
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.database.repository.superban import SuperbanRepository
from core.handlers.logs import sys_loggers
from core.utilities.strings import Strings

save_date = datetime.datetime.utcnow().isoformat()

@decorators.owner.init
@decorators.delete.init
def init(update, context):
    #Variables
    bot = context.bot
    text = update.message.text
    chat = update.effective_chat.id
    operator_id = update.message.from_user.id
    #Build a Keyboard Buttons
    buttons = []
    buttons.append(InlineKeyboardButton('Spam', callback_data='mSpam'))
    buttons.append(InlineKeyboardButton('Scam', callback_data='mScam'))
    buttons.append(InlineKeyboardButton('Userbot', callback_data='mUserbot'))
    buttons.append(InlineKeyboardButton('Porn', callback_data='mPorn'))
    buttons.append(InlineKeyboardButton('Other', callback_data='mOther'))
    buttons.append(InlineKeyboardButton('Close', callback_data='closeMenu'))
    menu = build_menu(buttons,2)
    if update.message.reply_to_message:
        user_id = update.message.reply_to_message.from_user.id
        update.message.reply_to_message.reply_text("Select a reason for the Superban", reply_markup=InlineKeyboardMarkup(menu))
    else:
        input_user_id = text[2:].strip().split(" ", 1)
        user_id = input_user_id[0]
        try:
            if user_id != "":
                default_motivation = "Other"
                data = [(user_id,default_motivation,save_date,operator_id)]
                SuperbanRepository().add(data)
                bot.kick_chat_member(chat, user_id)
                msg = 'You got super banned <a href="tg://user?id={}">{}</a>\nGo to: https://squirrel-network.online/knowhere to search for blacklisted users'.format(user_id,user_id)
                message(update,context,msg)
                logs_text = Strings.SUPERBAN_LOG.format(user_id,default_motivation,save_date,operator_id)
                messageWithId(update,context,Config.DEFAULT_LOG_CHANNEL,logs_text)
                formatter = "Superban eseguito da: {}".format(operator_id)
                sys_loggers("[SUPERBAN_LOGS]",formatter,False,False,True)
            else:
                message(update,context,"Attention you can not superbanned without entering an ID!")
        except BadRequest:
            message(update,context,"Attention the user id you entered does not exist!")

@decorators.owner.init
def update_superban(update, context):
    bot = context.bot
    query = update.callback_query
    if query.data.startswith("m"):
        #Variables
        chat_id = query.message.chat_id
        operator_id = query.from_user.id
        user_id = query.message.reply_to_message.from_user.id
        motivation = query.data[1:]
        row = SuperbanRepository().getById(user_id)
        if row:
            text = "Attention already superbanned user!"
            query.edit_message_text(text, parse_mode='HTML')
        else:
            data = [(user_id,motivation,save_date,operator_id)]
            SuperbanRepository().add(data)
            #Kick the User
            bot.kick_chat_member(chat_id, user_id)
            #Edit Message Text after push the button
            msg = 'You got super banned <a href="tg://user?id={}">{}</a>\nGo to: https://squirrel-network.online/knowhere to search for blacklisted users'.format(user_id,user_id)
            query.edit_message_text(msg, parse_mode='HTML')
            #Telegram Logs
            logs_text = Strings.SUPERBAN_LOG.format(user_id,motivation,save_date,operator_id)
            messageWithId(update,context,Config.DEFAULT_LOG_CHANNEL,logs_text)
            #System Logs
            formatter = "Superban eseguito da: {}".format(operator_id)
            sys_loggers("[SUPERBAN_LOGS]",formatter,False,False,True)
    if query.data == 'closeMenu':
        query.edit_message_text("You have closed the Menu", parse_mode='HTML')