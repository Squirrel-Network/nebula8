#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
     ###########################
     ##   DATABASE SETTINGS  ##
     ##########################
     HOST = os.environ.get('MYSQL_HOST', 'localhost')
     PORT = int(os.environ.get('MYSQL_PORT', '3306'))
     USER = os.environ.get('MYSQL_USER', 'root')
     PASSWORD = os.environ.get('MYSQL_PASSWORD')
     DBNAME = os.environ.get('MYSQL_DBNAME')
     ##########################
     ##   REDIS SETTINGS   ##
     ##########################
     RD_HOST = os.environ.get('REDIS_HOST', 'localhost')
     RD_PORT = os.environ.get('REDIS_PORT', '6379')
     RD_PASSWORD = os.environ.get('REDIS_PASSWORD')
     RD_DB = os.environ.get('REDIS_DB', 0)
     ###########################
     ##   TELEGRAM SETTINGS  ##
     ##########################
     BOT_TOKEN = os.environ.get('TOKEN')
     DEFAULT_WELCOME = os.environ.get('TG_DEFAULT_WELCOME', 'Welcome {} to the {} group')
     DEFAULT_RULES = os.environ.get('TG_DEFAULT_RULES', 'https://github.com/Squirrel-Network/GroupRules')
     DEFAULT_LOG_CHANNEL = os.environ.get('TG_DEFAULT_LOG_CHANNEL')
     DEFAULT_STAFF_GROUP = os.environ.get('TG_DEFAULT_STAFF_GROUP')
     ##########################
     ##   PROJECT SETTINGS   ##
     ##########################
     OPENWEATHER_API = os.environ.get('OPENWEATHER_TOKEN')
     ENABLE_PLUGINS = True
     DEFAULT_LANGUAGE = "EN"
     VERSION = '8.5.4'
     VERSION_NAME = 'Hatterene'
     REPO = 'https://github.com/Squirrel-Network/nebula8'
     DEVELOPER_CHAT_ID = os.environ.get('DEV_CHAT_ID')
     DEBUG = False
     if BOT_TOKEN is None:
          print("The environment variable TOKEN was not set correctly!")
          quit(1)
     if RD_PASSWORD is None:
          print("The environment variable REDIS_PASSWORD was not set correctly!")
          quit(1)
     if DEFAULT_LOG_CHANNEL is None:
          print("The environment variable TG_DEFAULT_LOG_CHANNEL was not set correctly!")
          quit(1)
     if DEFAULT_STAFF_GROUP is None:
          print("The environment variable TG_DEFAULT_STAFF_GROUP was not set correctly!")
          quit(1)
     if OPENWEATHER_API is None:
          print("The environment variable OPENWEATHER_TOKEN was not set correctly! this will not allow the weather plugin to work")
