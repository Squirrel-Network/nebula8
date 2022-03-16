#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
import pymysql
from pymysql import OperationalError
from config import Config
from loguru import logger

"""
This class handles database connection and inbound queries
"""
class Connection:
    def __init__(self):
        try:
            self.con = pymysql.connect(
                host = Config.HOST,
                port = Config.PORT,
                user = Config.USER,
                password = Config.PASSWORD,
                db = Config.DBNAME,
                autocommit=True,
                charset = 'utf8mb4',
                cursorclass = pymysql.cursors.DictCursor
                )
            self.cur = self.con.cursor()
        except OperationalError as e:
            logger.error(e)
            args = e.args
            self.con = pymysql.connect(
                host = Config.HOST,
                port = Config.PORT,
                user = Config.USER,
                password = Config.PASSWORD,
                autocommit=True,
                charset = 'utf8mb4',
                cursorclass = pymysql.cursors.DictCursor
                )
            #PSEUDO MIGRATIONS
            if args[0] == 1049:
                self.cur = self.con.cursor()
                exec_query = self.cur
                exec_query.execute('CREATE DATABASE IF NOT EXISTS nebula')
                exec_query.execute('CREATE TABLE nebula.owner_list (id int(11) NOT NULL,tg_id varchar(255) NOT NULL,tg_username varchar(255) NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4')
                exec_query.execute('CREATE TABLE nebula.users (id int(11) NOT NULL,tg_id varchar(50) NOT NULL,tg_username varchar(50) NOT NULL,created_at datetime NOT NULL,updated_at datetime NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4')
                logger.info('I created the nebula database')
                quit(1)

    def _select(self,sql,args=None):
        self.cur.execute(sql,args)
        self.sel = self.cur.fetchone()
        self.cur.close()
        self.con.close()
        return self.sel

    def _selectAll(self,sql,args=None):
        self.cur.execute(sql,args)
        self.sel = self.cur.fetchall()
        self.cur.close()
        self.con.close()
        return self.sel

    def _insert(self,sql,args=None):
        self.ins = self.cur.executemany(sql,args)
        return self.ins

    def _single_insert(self,sql,args=None):
        self.sins = self.cur.execute(sql,args)
        return self.sins

    def _dict_insert(self, sql, dictionary):
        self.dins = self.cur.execute(sql, list(dictionary.values()))
        return self.dins

    def _update(self,sql, args=None):
        self.upd = self.cur.executemany(sql,args)
        return self.upd

    def _delete(self, sql, args=None):
        self.delete = self.cur.executemany(sql,args)
        return self.delete