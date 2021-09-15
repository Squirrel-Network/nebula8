#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core.database.db_connect import Connection
from pypika import Query, Table

community = Table("community")

class CommunityRepository(Connection):
    def getAll(self):
        query = Query.from_(community).select("*")
        q = query.get_sql(quote_char=None)
        return self._selectAll(q)

    def getById(self, args=None):
        query = Query.from_(community).select("*").where(community.tg_group_id == '%s')
        q = query.get_sql(quote_char=None)

        return self._select(q, args)

    def update(self, args=None):
        q = "UPDATE community SET tg_group_name = %s WHERE tg_group_id = %s"
        return self._update(q, args)

    def add(self, args=None):
        q = "INSERT INTO community(tg_group_name, tg_group_id, tg_group_link, language, type) VALUES (%s,%s,%s,%s,%s)"
        return self._insert(q, args)