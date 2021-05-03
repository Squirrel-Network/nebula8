from core.database.db_connect import Connection
from pypika import Query, Table

superban = Table("superban_table")
whitelist = Table("whitelist_table")

class SuperbanRepository(Connection):
    def getById(self, args=None):
        query = Query.from_(superban).select("*").where(superban.user_id == '%s')
        q = query.get_sql(quote_char=None)

        return self._select(q, args)

    def getWhitelistById(self, args=None):
        query = Query.from_(whitelist).select("*").where(whitelist.tg_id == '%s')
        q = query.get_sql(quote_char=None)

        return self._select(q, args)

    def getAll(self, args=None):
        query = Query.from_(superban).select("user_id").where(superban.user_id == '%s')
        q = query.get_sql(quote_char=None)

        return self._selectAll(q, args)

    def add(self, args=None):
        q = "INSERT IGNORE INTO superban_table(user_id, motivation_text, user_date, id_operator) VALUES (%s,%s,%s,%s)"
        return self._insert(q, args)