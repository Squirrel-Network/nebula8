#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
import time
import datetime
from core.utilities.message import message
from core.handlers.welcome import welcome_bot
from core.handlers.logs import telegram_loggers, sys_loggers, debug_channel
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
    get_group = GroupRepository().getById(chat_id)
    record_title = GroupRepository.SET_GROUP_NAME
    entities = list(update.effective_message.entities)
    get_chat_tg = bot.getChat(chat_id=chat_id)
    linked_chat = get_chat_tg.linked_chat_id
    group_members_count = update.effective_chat.get_member_count()
    #buttons = list(update.effective_message.reply_markup.inline_keyboard)

    """
    This function updates the group id on the database
    when a group changes from group to supergroup
    """
    if update.effective_message.migrate_from_chat_id is not None:
        old_chat_id = update.message.migrate_from_chat_id
        new_chat_id = update.message.chat.id
        data = [(new_chat_id, old_chat_id)]
        GroupRepository().update(data)
        message(update,context,"<b>#Automatic handler:</b>\nThe chat has been migrated to <b>supergroup</b> the bot has made the modification on the database.\n<i>It is necessary to put the bot admin</i>")
        debug_channel(update,context,"[DEBUG_LOGGER] La chat {} è stata modifica da Gruppo a Supergruppo il suo nuovo id è: {}".format(old_chat_id,new_chat_id))
    """
    This function saves the group to the database
    when the bot is added as soon as a group or supergroup is created
    """
    if update.effective_message.group_chat_created == True or update.effective_message.supergroup_chat_created == True:
        welcome_bot(update,context)
        l_txt = "#Log <b>Bot added to group</b> {}\nId: <code>{}</code>".format(chat_title,chat_id)
        telegram_loggers(update,context,l_txt)
    """
    This feature changes the chat title
    on the database when it is changed
    """
    if update.effective_message.new_chat_title:
        data = [(chat_title,chat_id)]
        GroupRepository().update_group_settings(record_title,data)
        debug_channel(update,context,"[DEBUG_LOGGER] La chat <code>[{}]</code> ha cambiato titolo".format(chat_id))

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
            debug_channel(update,context,"[DEBUG_LOGGER] La chat <code>[{}]</code> ha cambiato foto\nIl suo nuovo URL è: {}".format(chat_id,url))
    """
    This function saves the number
    of users in the group in the database
    """
    if group_members_count > 0:
        record_count = GroupRepository.SET_GROUP_MEMBERS_COUNT
        data = [(group_members_count,chat_id)]
        GroupRepository().update_group_settings(record_count,data)
    """
    This function checks if the group is present in the blacklist
    if it is present the bot leaves the group
    """
    if check_group_blacklist(update) == True:
        message(update,context,"<b>#Automatic handler:</b>\nThe group is blacklisted the bot will automatically exit the chat")
        log_txt = "#Log <b>Bot removed from group</b> {}\nId: <code>{}</code>".format(chat_title,chat_id)
        telegram_loggers(update,context,log_txt)
        time.sleep(2)
        bot.leave_chat(chat_id)
        debug_channel(update,context,"[DEBUG_LOGGER] Il bot è stato rimosso dalla chat <code>[{}]</code> perchè il gruppo è in Blacklist".format(chat_id))
    """
    This function checks the
    badwords of the group
    """
    if check_group_badwords(update) == True:
        user = user_object(update)
        bot.delete_message(update.effective_message.chat_id, update.message.message_id)
        message(update,context,"<b>#Automatic handler:</b>\n<code>{}</code> You used a forbidden word!".format(user.id))
        debug_channel(update,context,"[DEBUG_LOGGER] L'utente <code>{}</code> ha usato una parola proibita".format(user.id))
    """
    This function checks if there is a badword in a link
    """
    if entities is not None:
        for x in entities:
            if x['url'] is not None:
                bad_word = x['url']
                row = GroupRepository().get_group_badwords([bad_word, chat_id])
                if row:
                    user = user_object(update)
                    bot.delete_message(update.effective_message.chat_id, update.message.message_id)
                    message(update,context,"<b>#Automatic handler:</b>\n<code>{}</code> You used a forbidden word!".format(user.id))
    """
    This function checks if messages
    are arriving from a channel and deletes them
    """
    if update.effective_message.sender_chat and get_group['sender_chat_block'] == 1:
        sender_chat_obj = update.effective_message.sender_chat

        if update.effective_message.voice_chat_started:
            return
        elif update.effective_message.voice_chat_ended:
            return
        elif get_chat_tg.type == "channel":
            return
        elif sender_chat_obj.id == linked_chat:
            return
        else:
            message(update,context,"<b>#Automatic Handler:</b>\nIn this group <code>[{}]</code> it is not allowed to write with the\n{} <code>[{}]</code> channel".format(chat_id,sender_chat_obj.title,sender_chat_obj.id))
            bot.delete_message(update.effective_message.chat_id, update.message.message_id)
    """
    This function checks that the bot is an administrator
    and sends an alert
    """
    if get_bot.status == 'member':
        message(update,context,"I am not an administrator of this group, you have to make me an administrator to function properly!")
        debug_channel(update,context,"[DEBUG_LOGGER] Il bot non è un amministratore della chat {}".format(chat_id))

    """
    This function is used to filter messages with spoiler type
    and delete them if the group owner puts the block at 1
    """
    for a in entities:
        type_entities = a['type']
        if type_entities is not None:
            if type_entities == "spoiler" and get_group['spoiler_block'] == 1:
                message(update,context,"<b>#Automatic Handler:</b>\nIn this chat the use of spoilers is not allowed!")
                bot.delete_message(update.effective_message.chat_id, update.message.message_id)
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