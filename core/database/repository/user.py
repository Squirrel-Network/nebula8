from core.database.db_connect import Connection
from core.database.QB import QB


class UserRepository(Connection):
    def getById(self, args=None):
        query = QB("users").select().columns(["*"])
        query = query.where("user_id", "=", "%s").buildQuery()

        return self._select(query, args)

    def getAll(self, args=None):
        query = QB("users").select().columns(["*"])
        query = query.where("user_id", "=", "%s").buildQuery()

        return self._selectAll(query, args)

    def add(self, args=None):
        # TODO: write add function
        return ''

    def update(self, username):
        # TODO: write update function
        return ''