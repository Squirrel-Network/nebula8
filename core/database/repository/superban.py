from core.database.db_connect import Connection
from core.database.QB import QB

class SuperbanRepository(Connection):
    def getById(self, args=None):
        query = QB("superban_table").select().columns(["*"])
        query = query.where("user_id", "=", "%s").buildQuery()

        return self._select(query, args)

    def getAll(self, args=None):
        query = QB("superban_table").select().columns(["user_id"])
        query = query.where("user_id", "=", "%s").buildQuery()

        return self._selectAll(query, args)