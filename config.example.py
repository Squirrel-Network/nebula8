#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

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
     DEFAULT_WELCOME = "Welcome {} to the {} group"
     DEFAULT_RULES = "https://github.com/Squirrel-Network/GroupRules"
     DEFAULT_LOG_CHANNEL = -123456789
     DEFAULT_STAFF_GROUP = -123456789
     ###########################
     ##   PROJECT SETTINGS   ##
     ##########################
     OPENWEATHER_API = 'Insert Token'
     ENABLE_PLUGINS = True
     DEFAULT_LANGUAGE = "EN"
     VERSION = '8.1.2'
     VERSION_NAME = 'Hatterene'
     REPO = 'https://github.com/Squirrel-Network/nebula8'
     DEBUG = True