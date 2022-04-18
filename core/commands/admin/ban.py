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
	delete_message_reply,
	reply_member_status_object)
from core.utilities.message import message
from core.utilities.strings import Strings
from core.utilities.monads import (
	Given,
	Try)
from telegram.utils.helpers import mention_html
from core.database.repository.group import GroupRepository
from languages.getLang import languages

def ban_error(update, context, username = None, id = None):
	message(
		update,
		context,
		"Si è verificato un problema per il ban dell'utente %s" % (username if username is not None else id))

def ban_success(update, context, username = None, id = None):
	message(update,context,"Ho bannato %s" % (username if username is not None else id))

@decorators.admin.user_admin
@decorators.delete.init
def init(update, context):
	languages(update,context)

	bot = bot_object(update,context)
	chat = update.effective_chat
	reply = update.message.reply_to_message
	if reply is not None:
		user_status = reply_member_status_object(update,context)
		user = reply.from_user
		row = GroupRepository().getById(chat.id)
		if user.id == bot.id:
			text = "I can't ban myself!"

			message(update,context,text)
		elif user_status.status == 'administrator' or user_status.status == 'creator':
			message(update,context,"I can't <i>ban</i> an administrator or creator!")
		else:
			if row['ban_message']:
				parsed_message = row['ban_message'].replace('{first_name}',
				user.first_name).replace('{chat}',
				update.message.chat.title).replace('{username}',
				"@"+user.username).replace('{mention}',mention_html(user.id, user.first_name)).replace('{userid}',str(user.id))
				ban_text = "{}".format(parsed_message)
			else:
				ban_text = languages.ban_message.format(
					user = reply.from_user.username or reply.from_user.first_name,
					userid = reply.from_user.id,
					chat = chat.title
				)
			#Log Ban
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

		if ban_argument[0] == '@':
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

@decorators.admin.user_admin
@decorators.delete.init
def set_ban_message(update, context):
    languages(update,context)
    record = GroupRepository.BAN_MESSAGE
    chat = update.effective_chat.id
    msg = update.message.text[7:]
    reply = update.message.reply_to_message
    if reply:
        ban_text = str(reply.text).lower()
        data = [(ban_text, chat)]
        GroupRepository().update_group_settings(record, data)
        message(update,context, text="Testo Ban impostato!")
    else:
        if msg != "":
            data = [(msg, chat)]
            GroupRepository().update_group_settings(record, data)
            message(update, context, "Hai Impostato il Messaggio Di Ban!")
        else:
            message(update, context, "Il testo del ban non può essere vuoto!")