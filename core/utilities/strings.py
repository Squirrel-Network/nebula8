#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
class Strings(object):
    ERROR_HANDLING = "Attention there was an error in sending the command\nContact support with the command /support"
    BAN_LOG = "<b>#Log User Banned!</b>\nUser_Id: {id}\n"\
              'Username: <a href="tg://user?id={id}">{username}</a>\n'\
              "Group: {chat}\n"
    SUPERBAN_LOG = "<b>#Log User Superbanned!</b>\nUser_Id: {}\nMotivation: {}\nDatetime: <code>{}</code>\nOperator_id: {}"
    REPORT_MSG = "#Report\nGroup Id: <code>{}</code>\nGroup Title: {}\nMessage: <i>{}</i>\nLink: {}"