#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
import psutil, datetime
import platform
from core import decorators
from core.utilities.message import message
from core.handlers.logs import sys_loggers

@decorators.owner.init
@decorators.delete.init
def init(update,context):
    msg = system_status()
    message(update,context,msg)
    formatter = "Eseguito da: {}".format(update.message.from_user.id)
    sys_loggers("[SERVER_INFO_LOGS]",formatter,False,False,True)

def system_status():
        cpu_percent = psutil.cpu_percent()
        memory_percent = psutil.virtual_memory()[2]
        disk_percent = psutil.disk_usage('/')[3]
        boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
        running_since = boot_time.strftime("%A %d. %B %Y")
        response = "<b>Server Status:</b>\n"
        response += "Current Disk_percent is: <code>{}%</code>\n".format(disk_percent)
        response += "Current CPU utilization is: <code>{}%</code>\n".format(cpu_percent)
        response += "Current memory utilization: <code>{}%</code>\n".format(memory_percent)
        response += "It's running since <b>{}</b>".format(running_since)
        return response