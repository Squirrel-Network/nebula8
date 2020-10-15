from core.database.db_connect import Connection
from pypika import Query, Table, Field


class UserRepository(Connection):
    def getById(self, args=None):
        users = Table("users")
        query = Query.from_(users).select("*").where(users.user_id == "%s").get_sql()

        return self._select(query, args)

    def getAll(self, args=None):
        users = Table("users")
        query = Query.from_(users).select("*").where(users.user_id == "%s").get_sql()

        return self._selectAll(query, args)

    def add(self, args=None):
        # TODO: write add function
        return ''

    def update(self, username):
        # TODO: write update function
        return ''