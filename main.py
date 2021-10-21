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
from telegram.ext import Updater
from core.commands import index
from plugins import plugin_index
from core import handlers
from core.handlers import handlers_index
from core.handlers.check_status_chat import check_updates

console = Console()
table = Table(show_header=True, header_style="bold blue")

# if version < 3.7, stop bot.
LOGGER = logging.getLogger(__name__)
if sys.version_info[0] < 3 or sys.version_info[1] < 7:
    LOGGER.error("You MUST have a python version of at least 3.7! Multiple features depend on this. Bot quitting.")
    quit(1)

# Print start with datetime
timestamp = datetime.strftime(datetime.today(), '%H:%M at %Y/%m/%d')
console.print("[bold blue][[[Welcome to Nebula Bot]]][/bold blue]")
table.add_column("[b]Date[/b]", style="dim", width=12)
table.add_column("[b]Plugins Status[/b]")

# Enable logging (In config.py DEBUG = True enable Debug Logging)
logging.basicConfig(
    level=(logging.INFO, logging.DEBUG)[Config.DEBUG], format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt="[%X]", handlers=[RichHandler()]
)
logger = logging.getLogger(__name__)

def main():
    updater = Updater(Config.BOT_TOKEN, use_context=True)
    dsp = updater.dispatcher
    job = updater.job_queue

    # I load all admin, user and owner commands
    index.user_command(dsp)
    index.admin_command(dsp)
    index.owner_command(dsp)
    #Plugins Section (if in the config.py ENABLE_PLUGINS is True it loads the plugins if ENABLE_PLUGINS is False it does not load them)
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
    # I load all handlers, commands without '/'
    handlers_index.core_handlers(dsp)
    handlers_index.jobs_handlers(job)
    handlers.logs.sys_loggers()
    # I load the error handler, when the bot receives an error it sends a private message to the developer
    dsp.add_error_handler(handlers.errors.error_handler)

    # Start the Bot Polling
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()