import psutil, datetime
from core import decorators
from core.utilities.strings import Strings
from core.utilities.message import message
from core.handlers.logs import sys_loggers

@decorators.owner.init
def init(update,context):
    msg = Strings.SERVER_INFO.format(
        cpu=psutil.cpu_percent(),
        ram=psutil.virtual_memory()[2],
        boot=datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))
    message(update,context,msg)
    formatter = "Eseguito da: {}".format(update.message.from_user.id)
    sys_loggers("[SERVER_INFO_LOGS]",formatter,False,False,True)