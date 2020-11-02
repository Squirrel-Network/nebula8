from core.database.repository.group import GroupRepository
from core.database.db_connect import Connection
from core import decorators

#metodo di INSERT
def insert_query(query,args):
    connector = Connection()
    print(args)
    sql = connector.cur.executemany(query,args)
    return sql


@decorators.owner.init
def init(update, context):
    chat = str(update.effective_chat.id)
    welcome = "Lorem Ipsum Dolor"
    rules = "Example Rules"
    community = 1
    lang = "EN"
    data = [(chat,welcome,rules,community,lang)]
    query = "INSERT INTO groups (id_group, welcome_text, rules_text, community, languages) VALUES (%s,%s,%s,%s,%s)"
    insert_query(query,data)