#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
import re
import datetime
from config import Config
from core import decorators
from core.utilities.menu import build_menu
from core.utilities.message import message
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
    operator_first_name = update.message.from_user.first_name
    save_date = datetime.datetime.utcnow().isoformat()
    #Build a Keyboard Buttons
    buttons = []
    buttons.append(InlineKeyboardButton('Spam', callback_data='mSpam'))
    buttons.append(InlineKeyboardButton('Scam', callback_data='mScam'))
    buttons.append(InlineKeyboardButton('Userbot', callback_data='mUserbot'))
    buttons.append(InlineKeyboardButton('Porn', callback_data='mPorn'))
    buttons.append(InlineKeyboardButton('Other', callback_data='mOther'))
    buttons.append(InlineKeyboardButton('Illegal Content', callback_data='mIllegal_Content'))
    buttons.append(InlineKeyboardButton('Harrasment', callback_data='mHarrasment'))
    buttons.append(InlineKeyboardButton('Remove Superban', callback_data='removeSuperban'))
    buttons.append(InlineKeyboardButton('Close', callback_data='closeMenu'))
    menu = build_menu(buttons,2)
    # Superban in response to a user
    if update.message.reply_to_message:
        user_id = update.message.reply_to_message.from_user.id
        update.message.reply_to_message.reply_text("Select a reason for the Superban", reply_markup=InlineKeyboardMarkup(menu))
    # Superban via id with optional motivation, format: /s 123456789 or /s 123456789 reason
    else:
        input_user_id = text[2:].strip().split(" ", 1)
        user_id = input_user_id[0]
        if user_id != "":
            number = re.search(Regex.HAS_NUMBER, user_id)
            if number is None:
                message(update,context,"Attention you must enter a number not letters!")
            else:
                row = SuperbanRepository().getById(int(user_id))
                if row:
                    message(update,context,"The user <code>{}</code> is already present in the database".format(user_id))
                else:
                    motivation_input = ""
                    if len(input_user_id) > 1:
                        motivation_input = input_user_id[1]
                        default_motivation = motivation_input
                    else:
                        default_motivation = "Other"
                    default_user_first_name = "NB{}".format(user_id)
                    data = [(user_id,default_user_first_name,default_motivation,save_date,operator_id,operator_username,operator_first_name)]
                    SuperbanRepository().add(data)
                    msg = '🚷 You got super banned <a href="tg://user?id={}">{}</a> via TelegramID\n\n📜 For the following reason: <b>{}</b>\n\n➡️ Go to: https://squirrel-network.online/knowhere/?q={} to search for blacklisted users'.format(user_id,user_id,default_motivation,user_id)
                    message(update,context,msg)

                    #Log in Telegram Channel
                    logs_text = Strings.SUPERBAN_LOG.format(default_user_first_name,user_id,default_motivation,save_date,operator_first_name,operator_username,operator_id)
                    message(update, context, logs_text, 'HTML', 'messageid', Config.DEFAULT_LOG_CHANNEL, None)

                    #Log in Debug Channel
                    formatter = "Superban eseguito da: {}[<code>{}</code>] verso l'utente: [<code>{}</code>]".format(operator_username,operator_id,user_id)
                    sys_loggers("[SUPERBAN_LOGS]",formatter,False,False,True)
                    debug_channel(update, context, "[DEBUG_LOGGER] {}".format(formatter))
        else:
            message(update,context,"Attention you can not superbanned without entering an TelegramID!")

@decorators.owner.init
def multi_superban(update,context):
    txt = update.message.text
    x = re.findall(r'\d+', txt)
    string = "MultiSuperban eseguito! dei seguenti id:\n"
    for a in x:
        save_date = datetime.datetime.utcnow().isoformat()
        default_motivation = "MultiSuperban"
        default_user_first_name = "NB{}".format(a)
        operator_id = update.message.from_user.id
        operator_username = "@"+update.message.from_user.username
        operator_first_name = update.message.from_user.first_name
        data = [(a,default_user_first_name,default_motivation,save_date,operator_id,operator_username,operator_first_name)]
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
        operator_first_name = query.from_user.first_name
        user = query.message.reply_to_message.from_user
        motivation = query.data[1:]
        row = SuperbanRepository().getById(user.id)
        whitelist = SuperbanRepository().getWhitelistById(user.id)
        if whitelist:
            text_w = "user {} is whitelisted you cannot blacklist!".format(user.first_name)
            query.edit_message_text(text_w, parse_mode='HTML')
        elif row:
            text = "Attention already <b>SuperBanned</b> user {} [<code>{}</code>]!".format(user.first_name,user.id)
            query.edit_message_text(text, parse_mode='HTML')
        else:
            data = [(user.id,user.first_name,motivation,save_date,operator_id,operator_username,operator_first_name)]
            SuperbanRepository().add(data)
            #Ban the User
            bot.ban_chat_member(chat_id, user.id)
            #Edit Message Text after push the button
            msg = '🚷 Got <b>SuperBanned</b> <a href="tg://user?id={}">{}</a>\n\n📝 For the following reason: <b>{}</b>\n\n➡ Go to: https://squirrel-network.online/knowhere?q={} to search for blacklisted users'.format(user.id,user.first_name,motivation,user.id)
            query.edit_message_text(msg, parse_mode='HTML')
            bot.delete_message(chat_id, query.message.reply_to_message.message_id)
            #Telegram Logs
            logs_text = Strings.SUPERBAN_LOG.format(user.first_name,user.id,motivation,save_date,operator_first_name,operator_username,operator_id)
            message(update, context, logs_text, 'HTML', 'messageid', Config.DEFAULT_LOG_CHANNEL, None)
            #System Logs
            formatter = "Superban eseguito dall'operatore: {}<code>[{}]</code>\nVerso l'utente: {} [<code>{}</code>]\nNella chat: [<code>{}</code>]".format(operator_username,operator_id,user.first_name,user.id,chat_id)
            sys_loggers("[SUPERBAN_LOGS]",formatter,False,False,True)
            debug_channel(update, context, "[DEBUG_LOGGER]\n{}".format(formatter))

    if query.data == "removeSuperban":
        user = query.message.reply_to_message.from_user
        row = SuperbanRepository().getById(user.id)
        if row:
            data = [(user.id)]
            SuperbanRepository().remove(data)
            msg = "I removed the superban to user {} [<code>{}</code>]".format(user.first_name,user.id)
            query.edit_message_text(msg,parse_mode='HTML')
        else:
            query.edit_message_text("Attention this user not super banned!!!",parse_mode='HTML')