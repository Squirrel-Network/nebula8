from core.database.db_connect import Connection
from pypika import Query, Table

groups = Table("groups")

class GroupRepository(Connection):
    ###### Column constants of the table ######
    SET_GROUP_NAME = "group_name"
    SET_WELCOME = "set_welcome"
    SET_SILENCE = "set_silence"
    SET_LANGUAGE = "languages"
    SET_USER_PROFILE_PICT = "set_user_profile_picture"
    SET_ARABIC = "set_arabic_filter"
    SET_CHINESE = "set_chinese_filter"
    SET_CIRILLIC = "set_cirillic_filter"
    SET_RULES_TEXT = "rules_text"
    SET_WELCOME_TEXT = "welcome_text"
    SET_LOG_CHANNEL = "log_channel"
    SET_MAX_WARN = "max_warn"
    # Filters
    EXE_FILTER = "exe_filter"
    GIF_FILTER = "gif_filter"

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

    # Save group by Welcome
    def add(self, args=None):
        #query = Query.into(groups).columns('id_group', 'welcome_text', 'rules_text', 'community', 'languages').insert('%s','%s','%s','%s',%s')
        #q = query.get_sql(quote_char=None)
        q = "INSERT INTO groups (id_group, group_name, welcome_text, welcome_buttons, rules_text, community, languages, set_welcome, max_warn, set_silence, exe_filter, block_new_member, set_arabic_filter, set_cirillic_filter, set_chinese_filter, set_user_profile_picture, gif_filter, log_channel) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        return self._insert(q, args)

    #TODO logic error
    def update(self, args=None):
        q = "UPDATE groups SET id_group = %s WHERE id_group = %s"
        return self._update(q, args)

    ##########################
    ##### GROUP SETTINGS #####
    ##########################

    def set_block_entry(self, args=None):
        q = "UPDATE groups SET set_welcome = %s, block_new_member = %s WHERE id_group = %s"
        return self._update(q, args)

    def update_group_settings(self, record, args=None):
        q = "UPDATE groups SET @record = %s WHERE id_group = %s".replace('@record',record)
        return self._update(q, args)