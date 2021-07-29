#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
import psutil, datetime, platform
from core import decorators
from core.utilities.message import message
from core.handlers.logs import sys_loggers

NAME_SERVER = "NAOS"

@decorators.owner.init
@decorators.delete.init
def init(update,context):
    msg = system_status()
    message(update,context,msg)
    formatter = "Eseguito da: {}".format(update.message.from_user.id)
    sys_loggers("[SERVER_INFO_LOGS]",formatter,False,False,True)

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def system_status():
        cpu_percent = psutil.cpu_percent()
        memory_percent = psutil.virtual_memory()[2]
        svmem = psutil.virtual_memory()
        boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
        partitions = psutil.disk_partitions()
        uname = platform.uname()
        cpufreq = psutil.cpu_freq()
        net_io = psutil.net_io_counters()
        running_since = boot_time.strftime("%A %d. %B %Y")
        response = "<b>{} Server Status:</b>\n\n".format(NAME_SERVER)
        response += "⚙️ ==== SYSTEM INFO ==== ⚙️\n"
        response += "System: <code>{}</code>\n".format(uname.system)
        response +="Node Name: <code>{}</code>\n".format(uname.node)
        response +="Release: <code>{}</code>\n".format(uname.release)
        response +="Version: <code>{}</code>\n".format(uname.version)
        response +="Machine: <code>{}</code>\n\n".format(uname.machine)
        response += "⚙️ ==== CPU INFO ==== ⚙️\n"
        response += "Current CPU utilization is: <code>{}%</code>\n".format(cpu_percent)
        response += "Current Frequency: <code>{}Mhz</code>\n".format(cpufreq.current)
        response += "Physical cores: <code>{}</code>\n".format(psutil.cpu_count(logical=False))
        response += "Total cores: <code>{}</code>\n\n".format(psutil.cpu_count(logical=True))
        response += "⚙️ ==== DISK INFO ==== ⚙️\n"
        for partition in partitions:
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                continue
            response += "Total Size: <code>{}</code>\n".format(get_size(partition_usage.total))
            response += "Used: <code>{}</code>\n".format(get_size(partition_usage.used))
            response += "Free: <code>{}</code>\n".format(get_size(partition_usage.free))
            response += "Current Disk_percent is: <code>{}%</code>\n\n".format(partition_usage.percent)
        response += "⚙️ ==== MEMORY INFO ==== ⚙️ \n"
        response += "Current memory utilization: <code>{}%</code>\n".format(memory_percent)
        response += "Total: <code>{}</code>\n\n".format(get_size(svmem.total))
        response += "⚙️ ==== NETWORK INFO ==== ⚙️ \n"
        response += "Total Bytes Sent: <code>{}</code>\n".format(get_size(net_io.bytes_sent))
        response += "Total Bytes Received: <code>{}</code>\n".format(get_size(net_io.bytes_recv))
        response += "It's running since <b>{}</b>".format(running_since)
        return response