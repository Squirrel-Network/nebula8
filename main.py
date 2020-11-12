#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
import logging
import sys
from rich.logging import RichHandler
from rich.console import Console
from rich.table import Table
from datetime import datetime
from config import Config
from telegram.ext import (Updater,Filters)
from core.commands import index
from plugins import plugin_index
from core import handlers
from core.handlers import handlers_index

console = Console()
table = Table(show_header=True, header_style="bold blue")

# if version < 3.6, stop bot.
LOGGER = logging.getLogger(__name__)
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error("You MUST have a python version of at least 3.6! Multiple features depend on this. Bot quitting.")
    quit(1)

# Print start with datetime
timestamp = datetime.strftime(datetime.today(), '%H:%M at %Y/%m/%d')
console.print("[bold blue][[[Welcome to Nebula Bot]]][/bold blue]")
table.add_column("[b]Date[/b]", style="dim", width=12)
table.add_column("[b]Plugins Status[/b]")

# Enable logging (set debug == logging.DEBUG ; set info == logging.INFO)
logging.basicConfig(
    level=(logging.INFO, logging.DEBUG)[Config.DEBUG], format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt="[%X]", handlers=[RichHandler()]
)
logger = logging.getLogger(__name__)

def main():
    updater = Updater(Config.BOT_TOKEN, use_context=True)
    dsp = updater.dispatcher

    index.user_command(dsp)
    index.admin_command(dsp)
    index.owner_command(dsp)
    #Plugins Section
    if Config.ENABLE_PLUGINS == True:
        plugin_index.function_plugins(dsp)
        table.add_row(
            "[yellow]{}[/yellow]".format(timestamp),
            "[green]Enable[/green]",
            )
        console.print(table)
    else:
        table.add_row(
            "[yellow]{}[/yellow]".format(timestamp),
            "[bold red]Disable[/bold red]",
            )
        console.print(table)

    handlers.logs.sys_loggers()
    handlers_index.core_handlers(dsp)

    dsp.add_error_handler(handlers.errors.error)

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()