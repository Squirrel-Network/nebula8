from core.database.db_connect import Connection

class GroupLanguageRepository(Connection):
    def getById(self,args=None):
        sql = "SELECT languages FROM groups WHERE id_group = %s"
        return self._select(sql, args)