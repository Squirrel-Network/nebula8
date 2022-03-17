#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

import redis
from config import Config
from loguru import logger

class RedisConnect():
    def __init__(self):
        try:
            self.con = redis.Redis(
                host=Config.RD_HOST,
                port=Config.RD_PORT,
                password=Config.RD_PASSWORD,
                db=Config.RD_DB
                )
        except Exception as e:
            logger.error(e)

    def hdel(self,key,field):
        self.con.hdel(key,field)

    def hexists(self,key,field):
        return self.con.hexists(key,field)

    def hget(self,key,field):
        return self.con.hget(key,field)

    def hset(self,key,field,value):
        self.con.hset(key,field,value)