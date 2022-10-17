#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core import decorators
from languages.getLang import languages
from core.utilities.strings import Strings
from core.utilities.message import message
from core.handlers.logs import telegram_loggers
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.utilities.menu import build_menu


@decorators.public.init
def init(update,context):
    bot = context.bot
    staff_group_id = -1001267698171
    buttons = []
    buttons.append(InlineKeyboardButton('Risolto✅', callback_data='resolved'))
    menu = build_menu(buttons,2)
    if update.effective_message.forward_date is not None:
        return

    chat = update.effective_chat
    languages(update,context)
    if str(update.effective_message.text).lower().startswith("@admin") or str(update.effective_message.text).lower().startswith("/report"):
        if update.effective_message.reply_to_message:
            msg = update.effective_message.reply_to_message
            format_link = "https://t.me/c/{}/{}".format(str(chat.id)[3:],msg.message_id)
            format_message = Strings.REPORT_MSG.format(chat.id,chat.title,msg.text,format_link)
            message(update, context, languages.report_msg, 'HTML', 'reply', None, None)
            telegram_loggers(update,context,format_message)
            bot.send_message(staff_group_id,format_message, reply_markup=InlineKeyboardMarkup(menu),parse_mode='HTML')
        else:
            msg_id = update.effective_message.message_id
            user_id = update.message.from_user.id
            user_first = update.message.from_user.first_name
            format_link = "https://t.me/c/{}/{}".format(str(chat.id)[3:],msg_id)
            format_message = '#Report\nUser: <a href="tg://user?id={}">{}</a>\nGroup Id: [<code>{}</code>]\nGroup Title: {}\nLink: {}'.format(user_id,user_first,str(chat.id)[3:],chat.title,format_link)
            message(update, context, languages.report_msg, 'HTML', 'reply', None, None)
            telegram_loggers(update,context,format_message)
            bot.send_message(staff_group_id,format_message, reply_markup=InlineKeyboardMarkup(menu),parse_mode='HTML')

@decorators.admin.user_admin
def update_resolve(update,context):
    query = update.callback_query
    var_message = query.message.text
    query.edit_message_text(text="{}\n<b>Risolto da: @{username}</b>"
    .format(var_message,username=str(update.effective_user.username)),parse_mode='HTML')