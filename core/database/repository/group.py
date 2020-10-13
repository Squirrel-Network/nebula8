from core.database.db_connect import Connection
from core.database.QB import QB


class GroupRepository(Connection):
    def getById(self, args=None):
        query = QB("groups").select().columns(["*"])
        query = query.where("id_group", "=", "%s").buildQuery()

        return self._select(query, args)

    def getAll(self,args=None):
        query = QB("groups").select().columns(["*"])
        query = query.where("id_group", "=", "%s").buildQuery()

        return self._selectAll(query, args)