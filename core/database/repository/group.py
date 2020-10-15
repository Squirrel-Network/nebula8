from core.database.db_connect import Connection
from pypika import Query, Table, Field


class GroupRepository(Connection):
    def getById(self, args=None):
        groups = Table("groups")
        query = Query.from_(groups).select("*").where(groups.id_group == "%s")

        return self._select(query, args)

    def getAll(self, args=None):
        query = Query.from_("groups").select("*")

        return self._selectAll(query, args)

    def insert(self, args=None):
        query = Query.from_("groups").insert("%s")

        return self._insert(query, args)
