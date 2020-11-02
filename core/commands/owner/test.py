from core.database.repository.group import GroupRepository
from core.database.db_connect import Connection
from core import decorators

def insert_query(query,args):
    connector = Connection()
    print(args)
    sql = connector.cur.executemany(query,args)
    return sql

@decorators.owner.init
def init(update, context):
    chat = str(update.effective_chat.id)
    test = "banana"
    data = [(chat,test)]
    query = "INSERT INTO prova (testo,testo_due) VALUES (%s,%s)"
    insert_query(query,data)