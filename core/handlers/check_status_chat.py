#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
import time
import datetime
from core.utilities.message import message
from core.handlers.welcome import welcome_bot
from core.handlers.logs import telegram_loggers, sys_loggers
from core.database.repository.group import GroupRepository
from core.database.repository.superban import SuperbanRepository
from core.utilities.functions import chat_object, user_object


def check_group_blacklist(update):
    chat_id = update.effective_chat.id
    row = SuperbanRepository().getGroupBlacklistById(chat_id)
    if row:
        return True
    else:
        return False

def check_group_badwords(update):
    chat_id = update.effective_chat.id
    bad_word = update.effective_message.text or update.effective_message.caption
    if bad_word is not None:
        row = GroupRepository().get_group_badwords([bad_word, chat_id])
        if row:
            return True
        else:
            return False

def check_status(update, context):
    bot = context.bot
    chat_title = update.effective_chat.title
    chat_id = update.effective_chat.id
    get_bot = bot.getChatMember(chat_id,bot.id)
    record_title = GroupRepository.SET_GROUP_NAME
    group_members_count = update.effective_chat.get_member_count()
    entities = list(update.effective_message.entities)
    #buttons = list(update.effective_message.reply_markup.inline_keyboard)

    if update.effective_message.migrate_from_chat_id is not None:
        old_chat_id = update.message.migrate_from_chat_id
        new_chat_id = update.message.chat.id
        data = [(new_chat_id, old_chat_id)]
        GroupRepository().update(data)
        message(update,context,"<b>#Automatic handler:</b>\nThe chat has been migrated to <b>supergroup</b> the bot has made the modification on the database.\n<i>It is necessary to put the bot admin</i>")

    if update.effective_message.group_chat_created == True or update.effective_message.supergroup_chat_created == True:
        welcome_bot(update,context)
        l_txt = "#Log <b>Bot added to group</b> {}\nId: <code>{}</code>".format(chat_title,chat_id)
        telegram_loggers(update,context,l_txt)

    if update.effective_message.new_chat_title:
        data = [(chat_title,chat_id)]
        GroupRepository().update_group_settings(record_title,data)

    """
    When a chat room changes group image it is saved to the webserver
    like this: example.com/group_photo/-100123456789.jpg (url variable)
    """
    if update.effective_message.new_chat_photo:
        chat = chat_object(update)
        if chat.type == "supergroup" or chat.type == "group":
            file_id = update.message.new_chat_photo[2].file_id
            newFile = bot.get_file(file_id)
            newFile.download('/var/www/naos.hersel.it/group_photo/{}.jpg'.format(chat_id))
            url = "https://naos.hersel.it/group_photo/{}.jpg".format(chat_id)
            data = [(url,chat_id)]
            record = GroupRepository.SET_GROUP_PHOTO
            GroupRepository().update_group_settings(record,data)
            formatter = "New Url: {}".format(url)
            sys_loggers("[UPDATE_GROUP_PHOTO_LOGS]",formatter,False,True)

    if group_members_count > 0:
        record_count = GroupRepository.SET_GROUP_MEMBERS_COUNT
        data = [(group_members_count,chat_id)]
        GroupRepository().update_group_settings(record_count,data)

    if check_group_blacklist(update) == True:
        message(update,context,"<b>#Automatic handler:</b>\nThe group is blacklisted the bot will automatically exit the chat")
        log_txt = "#Log <b>Bot removed from group</b> {}\nId: <code>{}</code>".format(chat_title,chat_id)
        telegram_loggers(update,context,log_txt)
        time.sleep(2)
        bot.leave_chat(chat_id)

    if check_group_badwords(update) == True:
        user = user_object(update)
        bot.delete_message(update.effective_message.chat_id, update.message.message_id)
        message(update,context,"<b>#Automatic handler:</b>\n<code>{}</code> You used a forbidden word!".format(user.id))

    if entities is not None:
        for x in entities:
            if x['url'] is not None:
                bad_word = x['url']
                row = GroupRepository().get_group_badwords([bad_word, chat_id])
                if row:
                    user = user_object(update)
                    bot.delete_message(update.effective_message.chat_id, update.message.message_id)
                    message(update,context,"<b>#Automatic handler:</b>\n<code>{}</code> You used a forbidden word!".format(user.id))

    if get_bot.status == 'member':
        message(update,context,"I am not an administrator of this group, you have to make me an administrator to function properly!")
    #TODO NONETYPE PROBLEM
    """if buttons is not None:
        for url in buttons:
            if url[0]['url'] is not None:
                bad_word = url[0]['url'] or url[0]['text']
                row = GroupRepository().get_group_badwords([bad_word, chat_id])
                if row:
                    user = user_object(update)
                    bot.delete_message(update.effective_message.chat_id, update.message.message_id)
                    message(update,context,"<b>#Automatic handler:</b>\n<code>{}</code> You used a forbidden word!".format(user.id))
    else:
        print("no button")"""


"""
this function has the task of saving
in the database the updates
for the calculation of messages
"""
def check_updates(update):
      chat = chat_object(update)
      user = user_object(update)
      date = datetime.datetime.utcnow().isoformat()
      if chat.type == "supergroup" or chat.type == "group":
          data = [(update.update_id, chat.id, user.id, date)]
          GroupRepository().insert_updates(data)