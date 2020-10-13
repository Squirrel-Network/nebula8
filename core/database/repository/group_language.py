from core.database.db_connect import Connection
from core.database.QB import QB


class GroupLanguageRepository(Connection):
    def getById(self, args=None):
        query = QB("groups").select().columns(["languages"])
        query = query.where("id_group", "=", "%s").buildQuery()

        return self._select(query, args)