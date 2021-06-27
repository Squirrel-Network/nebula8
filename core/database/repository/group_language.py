#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core.database.db_connect import Connection
from pypika import Query, Table


class GroupLanguageRepository(Connection):
    def getById(self, args=None):
        groups = Table("groups")
        query = Query.from_(groups).select(groups.languages).where(groups.id_group == '%s')
        q = query.get_sql(quote_char=None)

        return self._select(q, args)