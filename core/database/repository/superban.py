from core.database.db_connect import Connection
from pypika import Query, Table, Field

class SuperbanRepository(Connection):
    def getById(self, args=None):
        superban_table = Table("superban_table")
        query = Query.from_(superban_table).select("*").where(superban_table.user_id == "%s").get_sql()

        return self._select(query, args)

    def getAll(self, args=None):
        superban_table = Table("superban_table")
        query = Query.from_(superban_table).select("user_id").where(superban_table.user_id == "%s").get_sql()

        return self._selectAll(query, args)