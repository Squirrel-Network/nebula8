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
from core.utilities.monads import (
	Given,
	Try)
from languages.getLang import languages

def ban_error(update, context, username = None, id = None):
	message(
		update,
		context,
		"Si è verificato un problema per il ban dell'utente %s" % (username if username is not None else id))

def ban_success(update, context, username = None, id = None):
	message(
		update,
		context,
		"Ho bannato %s" % (username if username is not None else id))

@decorators.admin.user_admin
@decorators.delete.init
def init(update, context):
	languages(update,context)

	bot = bot_object(update,context)
	chat = update.effective_chat
	reply = update.message.reply_to_message

	if reply is not None:
		if reply.from_user.id == bot.id:
			text = "Non posso bannarmi da sola!"

			message(update,context,text)
		else:
			ban_text = languages.ban_message.format(
				user = reply.from_user.username or reply.from_user.first_name,
				userid = reply.from_user.id,
				chat = chat.title
			)

			logs_text = Strings.BAN_LOG.format(
				username = reply.from_user.username or reply.from_user.first_name,
				id = reply.from_user.id,
				chat = chat.title
			)

			delete_message_reply(update,context)
			ban_user_reply(update,context)
			message(update,context,ban_text)
			telegram_loggers(update,context,logs_text)

			formatter = "Ban eseguito da: {} nella chat {}".format(
				update.message.from_user.id,
				chat.title)

			sys_loggers("[BAN_LOGS]",formatter,False,True)
	else:
		ban_argument = update.message.text[5:]

		is_user_id = Try.of(lambda: int(ban_argument)).valueOf() is not None

		if ban_argument[0] is '@':
			username = ban_argument

			Try.of(lambda: ban_user_by_username(update, context, username)) \
				.catch(lambda err: ban_error(update, context, username = username)) \
				.map(lambda x : ban_success(update, context, username = username))
		elif is_user_id:
			userid = ban_argument

			Try.of(lambda: ban_user_by_id(update, context, userid)) \
				.catch(lambda err: ban_error(update, context, id = userid)) \
				.map(lambda x : ban_success(update, context, id = userid))
		else:
			message(
				update,
				context,
				"Sintassi del comando errata o utente non riconosciuto: {}"
					.format(ban_argument)
			)
			return