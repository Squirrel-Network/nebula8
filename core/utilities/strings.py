#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

class Strings(object):
    ERROR_HANDLING = "Attention I detected a problem to send the message in the following group:\n ID: <code>{}</code>\nTYPE: {}"
    BAN_LOG = "<b>⚠️ #Log User Banned!</b>\n👤 User_Id: <code>{id}</code>\n"\
              '👤 Username: <a href="tg://user?id={id}">{username}</a>\n'\
              "👥 Group: {chat}\n"
    SUPERBAN_LOG = '<b>🚷 #Log User Superbanned!</b>\n👤 User: {}[<code>{}</code>]\n📜 Reason: {}\n🕐 Datetime: <code>{}</code>\n👮‍♀️ Operator: {}\n{} [<code>{}</code>]'
    REPORT_MSG = "⚠️#Report\nGroup Id: <code>{}</code>\nGroup Title: {}\nMessage: <i>{}</i>\n📎 Link: {}"
    SOURCE = "<b>Hi! my name is: {}\nMy Version is: <code>{} {}</code>\nMy repository is: {}</b>"
    USER_INFO = '<b>⚙️ INFO USER:</b>\n👤 UserId: <code>{id}</code>\n👤 Username: <a href="tg://user?id={id}">{username}</a>\n⚠️ Warn: <code>{warn}</code>\n👥 Group: {chat}'
    WELCOME_BOT = "Thanks for adding me to the group ❤️\nPlease select your language => [/lang]\n\n❇️ Remember to make me administrator to work properly❗️\n\n🆘 Need Help? => /help\n\n⚙️ To change the group settings, press the [/settings] command\n\n⚙️ To change the filters in the group, type [/filters]\n\n⚙️ To change the warn limit in the group, type [/setwarn]\n\n⚙️ To change welcome type [/welcome] and follow the instructions\n\n<b>My Version is: {} {}</b>"