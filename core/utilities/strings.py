#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

class Strings(object):
    ERROR_HANDLING = "Attention there was an error in sending the command\nContact support with the command /report"
    BAN_LOG = "<b>#Log User Banned!</b>\nUser_Id: {id}\n"\
              'Username: <a href="tg://user?id={id}">{username}</a>\n'\
              "Group: {chat}\n"
    SUPERBAN_LOG = "<b>#Log User Superbanned!</b>\n👤 User_Id: [{}]\n📜 Reason: {}\n🕐 Datetime: <code>{}</code>\n👮‍♀️ Operator: {} [{}]"
    REPORT_MSG = "#Report\nGroup Id: <code>{}</code>\nGroup Title: {}\nMessage: <i>{}</i>\nLink: {}"
    SOURCE = "<b>Hi! my name is: {}\nMy Version is: <code>{} {}</code>\nMy repository is: {}</b>"
    USER_INFO = '<b>INFO USER:</b>\nUserId: <code>{id}</code>\nUsername: <a href="tg://user?id={id}">{username}</a>\nWarn: <code>{warn}</code>\nGroup: {chat}'
    WELCOME_BOT = "Thanks for adding me to the group\nPlease select your language => /lang\n\nRemember to make me administrator to work properly!\n\nNeed Help? => /help\n\nTo change the group settings, press the /settings command\nMy Version is: {} {}"