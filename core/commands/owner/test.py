from core.database.repository.group import GroupRepository
from core.database.db_connect import Connection
from core import decorators

def insert_query(query,args):
    connector = Connection()
    sql = connector.cur.execute(query,[args])
    return sql

@decorators.owner.init
def init(update, context):
    chat = str(update.message.chat_id)
    #connector = Connection()
    query = "INSERT INTO prova (testo) VALUES (%s)"
    insert_query(query,chat)
    #connector.cur.execute(query,[chat])