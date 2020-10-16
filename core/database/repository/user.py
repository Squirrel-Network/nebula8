from core.database.db_connect import Connection
from pypika import Query, Table, Field

users = Table("users")


class UserRepository(Connection):
    def getById(self, args=None):
        query = Query.from_(users).select("*").where(users.user_id == "%s")
        q = query.get_sql(quote_char=None)

        return self._select(q, args)

    def getAll(self, args=None):
        query = Query.from_(users).select("*").where(users.user_id == "%s")
        q = query.get_sql(quote_char=None)

        return self._selectAll(q, args)

    def add(self, args=None):
        # TODO: write add function
        return ''

    def update(self, username):
        # TODO: write update function
        return ''