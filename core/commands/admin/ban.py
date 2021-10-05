#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core import decorators
from core.handlers.logs import sys_loggers, telegram_loggers
from core.utilities.functions import (
	ban_user_reply,
	ban_user_by_username,
	ban_user_by_id,
	bot_object,
	delete_message_reply)
from core.utilities.message import message
from core.utilities.strings import Strings
from core.utilities.monads import Try
from core.utilities.parser import ArgumentProcesser
from languages.getLang import languages

def ban_error(update, context, username = None, id = None):
	languages(update,context)
	message(update,context,languages.ban_user_error % (username if username is not None else id))

def ban_success(update, context, chat, username = None, id = None):
	languages(update,context)
	message(update,context,languages.user_ban % (username if username is not None else id))
	logs_text = "<b>#Log User Banned!</b>\nGroup: {}\nUser: {}".format(chat.title,username or id)
	telegram_loggers(update,context,logs_text)

def ban_reply_error(update, context, username = None, id = None):
	ban_error(update, context, username, id)

def ban_reply_succes(update, context, chat, ban_text = None, logs_text = None):
	delete_message_reply(update, context)
	message(update,context,ban_text)
	telegram_loggers(update,context,logs_text)

	formatter = "Ban eseguito da: {} nella chat {}".format(
		update.message.from_user.id,
		chat.title)

	sys_loggers("[BAN_LOGS]",formatter,False,True)

def ban_by_reply(update, context, args):
	bot = bot_object(update,context)
	chat = update.effective_chat
	reply = update.message.reply_to_message

	if reply is not None:
		if reply.from_user.id == bot.id:
			message(update,context,languages.bot_ban)
		else:
			username = reply.from_user.username or reply.from_user.first_name

			ban_text = languages.ban_message.format(
				user = username,
				userid = reply.from_user.id,
				chat = chat.title
			)

			logs_text = Strings.BAN_LOG.format(
				username = username,
				id = reply.from_user.id,
				chat = chat.title
			)

			username = reply.from_user.username and ("@" + reply.from_user.username)
			firstname = reply.from_user.first_name

			Try.of(lambda: ban_user_reply(update,context)) \
				.catch(lambda err: ban_reply_error(update, context, username or firstname)) \
				.map(lambda x : ban_reply_succes(update, context, chat, username = username, ban_text=ban_text, logs_text=logs_text))

def ban_by_id(update, context, args):
	userid = args[0]
	chat = update.effective_chat

	Try.of(lambda: ban_user_by_id(update, context, userid)) \
		.catch(lambda err: ban_error(update, context, id = userid)) \
		.map(lambda x : ban_success(update, context, chat, id = userid))

def ban_by_user(update, context, args):
	username = args[0]
	chat = update.effective_chat

	Try.of(lambda: ban_user_by_username(update, context, username)) \
		.catch(lambda err: ban_error(update, context, username = username)) \
		.map(lambda x : ban_success(update, context, chat, username = username))

@decorators.admin.user_admin
@decorators.delete.init
def init(update, context):
	languages(update,context)

	options = [
		("", [], ban_by_reply),
		("int", [], ban_by_id),
		("user", [], ban_by_user)
	]

	ap = ArgumentProcesser(update.message.text, update, context)
	valid_command = ap.try_matches_execute(options)

	if not valid_command:
		usage = """Usage:
			/ban id:int
			/ban nick:user
			/ban
		"""
		message(update,context, usage)