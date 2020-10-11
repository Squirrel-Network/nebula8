from core.database.db_connect import Connection

class UserRepository(Connection):
    def getById(self, args=None):
        sql = "SELECT * FROM users WHERE user_id = %s"
        return self._selectAll(sql, args)

    def add(self, args=None):
        # TODO: write add function
        return ''

    def update(self, username):
        # TODO: write update function
        return ''
