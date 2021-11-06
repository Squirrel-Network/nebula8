#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core.database.db_connect import Connection
from pypika import Query, Table

superban = Table("superban_table")
whitelist = Table("whitelist_table")
group_blacklist = Table("groups_blacklist")

class SuperbanRepository(Connection):
    def getById(self, args=None):
        query = Query.from_(superban).select("*").where(superban.user_id == '%s')
        q = query.get_sql(quote_char=None)

        return self._select(q, args)

    def getWhitelistById(self, args=None):
        query = Query.from_(whitelist).select("*").where(whitelist.tg_id == '%s')
        q = query.get_sql(quote_char=None)

        return self._select(q, args)

    def getGroupBlacklistById(self, args=None):
        query = Query.from_(group_blacklist).select("*").where(group_blacklist.tg_id_group == '%s')
        q = query.get_sql(quote_char=None)

        return self._select(q, args)

    def addWhitelist(self, args=None):
        q = "INSERT IGNORE INTO whitelist_table(tg_id, tg_username) VALUES (%s,%s)"
        return self._insert(q, args)

    def getAll(self, args=None):
        query = Query.from_(superban).select("user_id").where(superban.user_id == '%s')
        q = query.get_sql(quote_char=None)

        return self._selectAll(q, args)

    def add(self, args=None):
        q = "INSERT IGNORE INTO superban_table(user_id, motivation_text, user_date, id_operator) VALUES (%s,%s,%s,%s)"
        return self._insert(q, args)

    def remove(self, args=None):
        q = "DELETE FROM superban_table WHERE user_id = %s"
        return self._delete(q, args)