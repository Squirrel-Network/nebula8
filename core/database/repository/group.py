from core.database.db_connect import Connection
from pypika import Query, Table

groups = Table("groups")

class GroupRepository(Connection):
    def getById(self, args=None):
        query = Query.from_(groups).select("*").where(groups.id_group == '%s')
        q = query.get_sql(quote_char=None)

        return self._select(q, args)

    def getAllById(self, args=None):
        query = Query.from_(groups).select("*").where(groups.id_group == '%s')
        q = query.get_sql(quote_char=None)

        return self._selectAll(q, args)

    def getAll(self):
        query = Query.from_(groups).select("*")
        q = query.get_sql(quote_char=None)

        return self._selectAll(q)

    def add(self, args=None):
        #query = Query.into(groups).columns('id_group', 'welcome_text', 'rules_text', 'community', 'languages').insert('%s','%s','%s','%s',%s')
        #q = query.get_sql(quote_char=None)
        q = "INSERT INTO groups (id_group, welcome_text, rules_text, community, languages) VALUES (%s,%s,%s,%s,%s)"
        return self._insert(q, args)

    #TODO logic error
    def update(self, args=None):
        q = "UPDATE groups SET id_group = %s WHERE id_group = %s"
        return self._update(q, args)

    def update_language(self, args=None):
        q = "UPDATE groups SET languages = %s WHERE id_group = %s"
        return self._update(q, args)