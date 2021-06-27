#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from languages.getLang import languages
from core.utilities.message import message
from core import decorators
from core.utilities.functions import bot_object, user_object

@decorators.private.init
@decorators.delete.init
def init(update, context):
    languages(update,context)
    bot = bot_object(update,context)
    user = user_object(update)
    get_user_lang = user.language_code
    if get_user_lang == 'it':
        message(update,context,
        "Ciao io mi chiamo {} e sono uno strumento per la gestione dei gruppi con tante funzioni speciali"\
            " tutte da scoprire! e sono Open Source! Se vuoi vedere il mio sorgente digita:"\
            " /source\nSe hai bisogno di aiuto digita /help".format("@"+bot.username))
    else:
        message(update,context,languages.start.format("@"+bot.username))