#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
import re
from core import decorators
from core.utilities.menu import build_menu
from core.database.repository.user import UserRepository
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.utilities.functions import user_object
from core.utilities.message import message
from core.utilities.regex import Regex

@decorators.private.init
def init(update,context):
    bot = context.bot
    user = user_object(update)
    main_text = UserRepository().getLinktreeMainText(int(user.id))
    if main_text:
        get_buttons = UserRepository().getLinkTreeButtons(user.id)
        buttons = []
        for row in get_buttons:
            buttons.append(InlineKeyboardButton(text=row['button_text'], url=row['button_url']))
        menu = build_menu(buttons, 1)
        msg = main_text['main_text']
        bot.send_message(update.message.from_user.id, msg, reply_markup=InlineKeyboardMarkup(menu), parse_mode="HTML")
    else:
        bot.send_message(update.message.from_user.id,"You have not created any Linktree, Create your Linktree using the command /startlink", parse_mode="HTML")

@decorators.private.init
def linktreeid(update,context):
    user = user_object(update)
    rows = UserRepository().getLinkTreeButtons(user.id)
    if rows:
        string = ""
        for row in rows:
            string += "▪️ ID: <code>{id}</code> TITLE: {title}\n".format(id=row['button_id'],title=row['button_text'])
        message(update,context,"List Buttons:\n{}".format(string))
    else:
        message(update,context,"You don't have any buttons you can insert buttons with the command <code>/addlink title,url</code>")

@decorators.private.init
def startlink(update,context):
    user = user_object(update)
    row = UserRepository().getLinktreeMainText(int(user.id))
    if row:
        message(update,context,"You have already used the command once view your links with /linktree")
    else:
        default_main_text = "Sample text, you can edit text with the command <code>/mainlink sampletext</code>"
        data = [(user.id,default_main_text)]
        UserRepository().insert_main_text_linktree(data)
        message(update, context,"You first created /linktree content\n\n🟦 Legend:\n🔹 To add a button type: <code>/addlink title,url</code>\n🔹 To see all links type: <code>/linktree</code>\n🔹 To change the main text type <code>/mainlink sampletext</code>\n🔹 To delete a button type <code>/deletelink id</code>\n<b>NB: to know the id of the buttons type the command /linktreeid</b>")
@decorators.private.init
def mainlink(update,context):
    user = user_object(update)
    msg = update.message.text[9:].strip()
    if msg != "":
        data = [(msg, user.id)]
        UserRepository().update_main_text_linktree(data)
        message(update, context, "You have edited the main text\nPreview: {}".format(msg))
    else:
        message(update,context,"Attention the message is empty!")

@decorators.private.init
def add_button(update,context):
    text = update.message.text
    user = user_object(update)
    try:
        input_text = text[8:].strip().split(",")
        title_button = input_text[0]
        url_button = input_text[1]
        is_url = re.search(Regex.HAS_URL, url_button)
        if is_url is None:
            message(update, context, "Attention you have to enter a correct URL format! Example: <code>https://google.it</code>")
        elif len(input_text) > 2:
            message(update, context,"You can only enter two parameters at a time!")
        else:
            data = [(user.id,str(title_button).strip(),str(url_button).strip())]
            UserRepository().insert_linktree_button(data)
            message(update,context,"You have inserted a new button in the <code>/linktree</code> command\n\n Button text: {buttontext}\n Button URL: {buttonurl}".format(buttontext=title_button,buttonurl=url_button))
    except IndexError:
        message(update,context,"You have forgotten one or more required parameters the correct format of the command is:\n <code>/addlink title,https://example.com</code>")

@decorators.private.init
def delete_button(update, context):
    user = user_object(update)
    text = update.message.text
    input_text = text[11:].strip().split(" ", 1)
    button_id = input_text[0]
    number = re.search(Regex.HAS_NUMBER, button_id)
    if number is None:
        message(update, context, "Attention you must enter a number not letters!")
    data = [(button_id,user.id)]
    UserRepository().delete_linktree_button(data)
    message(update,context,"You deleted the button with id: <code>{}</code>".format(button_id))

