import logging
from config import Config
from core.utilities.message import messageWithId

def sys_loggers(name="",message="",debugs = False,info = False,warning = False,errors = False, critical = False):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler('debug.log')
    fh.setLevel(logging.INFO)
    logger.addHandler(fh)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    if debugs == True:
        logger.debug(message)
    elif info == True:
        logger.info(message)
    elif warning == True:
        logger.warning(message)
    elif errors == True:
        logger.error(message)
    elif critical == True:
        logger.critical(message)

def telegram_loggers(update,context,msg = ""):
    id_channel = Config.DEFAULT_LOG_CHANNEL
    send = messageWithId(update,context,id_channel,msg)
    return send

def staff_loggers(update,context,msg = ""):
    id_staff_group = Config.DEFAULT_STAFF_GROUP
    send = messageWithId(update,context,id_staff_group,msg)
    return send