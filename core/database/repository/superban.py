from core.database.db_connect import Connection
from pypika import Query, Table, Field

superban = Table("superban_table")

class SuperbanRepository(Connection):
    def getById(self, args=None):
        query = Query.from_(superban).select("*").where(superban.user_id == '%s')
        q = query.get_sql(quote_char=None)

        return self._select(q, args)

    def getAll(self, args=None):
        query = Query.from_(superban).select("user_id").where(superban.user_id == '%s')
        q = query.get_sql(quote_char=None)

        return self._selectAll(q, args)