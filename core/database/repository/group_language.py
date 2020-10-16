from core.database.db_connect import Connection
from pypika import Query, Table, Field, Criterion


class GroupLanguageRepository(Connection):
    def getById(self, args=None):
        groups = Table("groups")
        query = Query.from_(groups).select(groups.languages).where(groups.id_group == -1001349066370)
        #debug
        print(query.get_sql(quote_char=None))

        return self._select(query, args)