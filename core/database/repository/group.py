from core.database.db_connect import Connection
from pypika import Query, Table, Field

groups = Table("groups")

class GroupRepository(Connection):
    def getById(self, args=None):
        query = Query.from_(groups).select("*").where(groups.id_group == "%s")
        q = query.get_sql(quote_char=None)

        return self._select(q, args)

    def getAll(self, args=None):
        query = Query.from_(groups).select("*").where(groups.id_group == "%s")
        q = query.get_sql(quote_char=None)

        return self._selectAll(q, args)

    def insert(self, args=None):
        query = Query.from_(groups).insert("%s")
        q = query.get_sql(quote_char=None)

        return self._insert(q, args)