#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core.database.db_connect import Connection
from pypika import Query, Table


dashboard = Table("nebula_dashboard")

class DashboardRepository(Connection):

    def getById(self, args=None):
        query = Query.from_(dashboard).select("*").where(dashboard.tg_id == "%s")
        q = query.get_sql(quote_char=None)

        return self._select(q, args)

    def getByGroupId(self, args=None):
        query = Query.from_(dashboard).select("*").where(dashboard.tg_group_id == "%s")
        q = query.get_sql(quote_char=None)

        return self._select(q, args)

    def getByUsername(self, args=None):
        q = "SELECT * FROM nebula_dashboard WHERE tg_username = %s"

        return self._select(q, args)

    def getUserAndGroup(self, args=None):
        q = "SELECT * FROM nebula_dashboard WHERE tg_group_id = %s AND tg_id = %s"

        return self._select(q, args)

    def add(self, args=None):
        q = "INSERT INTO nebula_dashboard (tg_id, tg_username, tg_group_id, enable, role, created_at, updated_at) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        return self._insert(q, args)

    def update(self, args=None):
        q = "UPDATE nebula_dashboard SET tg_username = %s, role = %s, updated_at = %s WHERE tg_id = %s AND tg_group_id = %s"
        return self._update(q, args)