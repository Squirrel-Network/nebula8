#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

import logging
import sys
from rich.logging import RichHandler
from rich.console import Console
from datetime import datetime
from config import Config
from telegram.ext import (Updater,Filters)
from core.commands import index
from plugins import plugin_index
from core import handlers
from core.handlers import handlers_index

console = Console()
# if version < 3.6, stop bot.
LOGGER = logging.getLogger(__name__)
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error("You MUST have a python version of at least 3.6! Multiple features depend on this. Bot quitting.")
    quit(1)

# Print start with datetime
timestamp = datetime.strftime(datetime.today(), '%H:%M at %Y/%m/%d')
console.print("[bold blue][[[Welcome to Nebula Bot]]][/bold blue]\n [yellow]Bot started on {}[/yellow]".format(timestamp))

# Enable logging (set debug == logging.DEBUG ; set info == logging.INFO)
logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt="[%X]", handlers=[RichHandler()]
)
logger = logging.getLogger(__name__)

def main():
    updater = Updater(Config.BOT_TOKEN, use_context=True)
    dsp = updater.dispatcher

    index.user_command(dsp)
    index.admin_command(dsp)
    index.owner_command(dsp)
    handlers_index.core_handlers(dsp)

    #Plugins Section
    if Config.ENABLE_PLUGINS == True:
        console.print("[b]PLUGINS STATUS:[/b] [green]Enable[/green]")
        plugin_index.function_plugins(dsp)
    else:
        console.print("[b]PLUGINS STATUS:[/b] [bold red]Disable[/bold red]")

    dsp.add_error_handler(handlers.errors.error)

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()