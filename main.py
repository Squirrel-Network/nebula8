#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
import sys
import pytz
import logging
from config import Config
from loguru import logger
from telegram.ext import Updater, Defaults
from telegram import ParseMode
from core.commands import index
from plugins import plugin_index
from core import handlers
from core.handlers import handlers_index
from tabulate import tabulate

# crea la tabella con i dati desiderati
table_data = [
    ["Type", "Description", "Extra"],
    ["Version", Config.VERSION, Config.VERSION_NAME],
    ["Author", "SquirrelNetwork", Config.REPO],
    ["Debug", Config.DEBUG],
    ["Plugins", "Enable"]
]

# stampa la tabella formattata




# if version < 3.7, stop bot.
LOGGING = logging.getLogger(__name__)
if sys.version_info[0] < 3 or sys.version_info[1] < 7:
    LOGGING.error("You MUST have a python version of at least 3.7! Multiple features depend on this. Bot quitting.")
    quit(1)

# Enable logging (In config.py DEBUG = True enable Debug Logging)
logging.basicConfig(level=(logging.INFO, logging.DEBUG)[Config.DEBUG], format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

@logger.catch
def main():
    """Instantiate a Defaults object"""
    defaults = Defaults(parse_mode=ParseMode.HTML, tzinfo=pytz.timezone('Europe/Rome'))
    updater = Updater(Config.BOT_TOKEN, defaults=defaults, workers=32)
    dsp = updater.dispatcher
    job_updater = updater.job_queue

    # I load all admin, user and owner commands
    index.user_command(dsp)
    index.admin_command(dsp)
    index.owner_command(dsp)

    #Plugins Section (if in the config.py ENABLE_PLUGINS is True it loads the plugins if ENABLE_PLUGINS is False it does not load them)
    if Config.ENABLE_PLUGINS == True :
        plugin_index.function_plugins(dsp)
        logger.info('Plugin Enabled')
    else:
        logger.info('Plugin Disabled')

    # I load all handlers, commands without '/'
    handlers_index.core_handlers(dsp)
    handlers.logs.sys_loggers()
    handlers.handlers_index.jobs_handlers(job_updater)
    # I load the error handler, when the bot receives an error it sends a private message to the developer
    dsp.add_error_handler(handlers.errors.error_handler)
    dsp.add_error_handler(handlers.handler_errors.init)

    # Start the Bot Polling
    updater.start_polling(poll_interval=1.0, timeout=5.0)
    updater.idle()

if __name__ == '__main__':
    main()