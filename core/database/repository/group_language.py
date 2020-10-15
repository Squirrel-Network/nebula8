from core.database.db_connect import Connection
from pypika import Query, Table, Field


class GroupLanguageRepository(Connection):
    def getById(self, args=None):
        groups = Table("groups")
        query = Query.from_(groups).select("languages")
        query = query.where(groups.id_group == "%s")

        return self._select(query, args)