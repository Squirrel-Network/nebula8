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

    # Save group by Welcome
    def add(self, args=None):
        #query = Query.into(groups).columns('id_group', 'welcome_text', 'rules_text', 'community', 'languages').insert('%s','%s','%s','%s',%s')
        #q = query.get_sql(quote_char=None)
        q = "INSERT INTO groups (id_group, welcome_text, welcome_buttons, rules_text, community, languages, set_welcome, max_warn, set_silence, exe_filter, block_new_member, set_arabic_filter, set_cirillic_filter, set_chinese_filter, set_user_profile_picture, gif_filter, log_channel) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        return self._insert(q, args)

    #TODO logic error
    def update(self, args=None):
        q = "UPDATE groups SET id_group = %s WHERE id_group = %s"
        return self._update(q, args)

    ##########################
    ##### GROUP SETTINGS #####
    ##########################
    def SetWelcome(self, args=None):
        q = "UPDATE groups SET set_welcome = %s WHERE id_group = %s"
        return self._update(q, args)

    def setSilence(self, args=None):
        q = "UPDATE groups SET set_silence = %s WHERE id_group = %s"
        return self._update(q, args)

    def setExeFilter(self, args=None):
        q = "UPDATE groups SET exe_filter = %s WHERE id_group = %s"
        return self._update(q, args)

    def setGifFilter(self, args=None):
        q = "UPDATE groups SET gif_filter = %s WHERE id_group = %s"
        return self._update(q, args)

    def update_language(self, args=None):
        q = "UPDATE groups SET languages = %s WHERE id_group = %s"
        return self._update(q, args)

    def set_block_entry(self, args=None):
        q = "UPDATE groups SET set_welcome = %s, block_new_member = %s WHERE id_group = %s"
        return self._update(q, args)

    def set_user_profile_photo(self, args=None):
        q = "UPDATE groups SET set_user_profile_picture = %s WHERE id_group = %s"
        return self._update(q, args)

    def set_arabic_filter(self, args=None):
        q = "UPDATE groups SET set_arabic_filter = %s WHERE id_group = %s"
        return self._update(q, args)

    def set_cirillic_filter(self, args=None):
        q = "UPDATE groups SET set_cirillic_filter = %s WHERE id_group = %s"
        return self._update(q, args)

    def set_chinese_filter(self, args=None):
        q = "UPDATE groups SET set_chinese_filter = %s WHERE id_group = %s"
        return self._update(q, args)

    def update_group_welcome(self, args=None):
        q = "UPDATE groups SET welcome_text = %s WHERE id_group = %s"
        return self._update(q, args)

    def update_log_channel(self, args=None):
        q = "UPDATE groups SET log_channel = %s WHERE id_group = %s"
        return self._update(q, args)