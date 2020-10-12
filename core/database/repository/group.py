from core.database.db_connect import Connection

class GroupRepository(Connection):
    def getById(self,args=None):
        sql = "SELECT * FROM groups WHERE id_group = %s"
        return self._select(sql, args)