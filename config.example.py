class Config(object):
     ###########################
     ##   DATABASE SETTINGS  ##
     ##########################
     HOST = 'localhost'
     PORT = 3306
     USER = 'usr'
     PASSWORD = 'pws'
     DBNAME = 'dbname'
     ###########################
     ##   TELEGRAM SETTINGS  ##
     ##########################
     BOT_TOKEN = 'INSERT TOKEN HERE'
     SUPERADMIN = {
          'foo': 123456789,
          'bar': 123456789
     }
     OWNER = {
          'foo': 123456789,
          'bar': 123456789
     }
     DEFAULT_LOG_CHANNEL = -123456789
     ###########################
     ##   PROJECT SETTINGS   ##
     ##########################
     ENABLE_PLUGINS = True
     DEFAULT_LANGUAGE = "EN"
     VERSION = '8.0.0'
     DEBUG = True