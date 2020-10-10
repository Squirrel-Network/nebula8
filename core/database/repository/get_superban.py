from core.database.db_connect import Connection

class SuperbanRepository(Connection):
    def getById(self,args=None):
        sql = "SELECT * FROM superban_table WHERE user_id = %s"
        return self._selectAll(sql, args)
    def getByIdFetchOne(self,args = None):
        sql = "SELECT user_id FROM superban_table WHERE user_id = %s"
        return self._select(sql, args)