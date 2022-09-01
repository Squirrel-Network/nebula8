#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core.database.db_connect import Connection
from pypika import Query, Table

groups = Table("groups")
whitelist_channels = Table("whitelist_channel")

class GroupRepository(Connection):
    ###### Column constants of the table ######
    SET_ID_GROUP = "id_group"
    SET_GROUP_NAME = "group_name"
    SET_WELCOME_TEXT  = "welcome_text"
    SET_WELCOME_BUTTONS = "welcome_buttons"
    SET_RULES_TEXT = "rules_text"
    SET_COMMUNITY = "community"
    SET_LANGUAGE = "languages"
    SET_WELCOME = "set_welcome"
    SET_MAX_WARN = "max_warn"
    SET_SILENCE = "set_silence"
    EXE_FILTER = "exe_filter"
    SET_BLOCK_N_M = "block_new_member"
    SET_ARABIC = "set_arabic_filter"
    SET_CIRILLIC = "set_cirillic_filter"
    SET_CHINESE = "set_chinese_filter"
    SET_USER_PROFILE_PICT = "set_user_profile_picture"
    GIF_FILTER = "gif_filter"
    SET_CAS_BAN = "set_cas_ban"
    SET_TPNU = "type_no_username"
    SET_LOG_CHANNEL = "log_channel"
    SET_GROUP_PHOTO = "group_photo"
    SET_GROUP_MEMBERS_COUNT = "total_users"
    ZIP_FILTER = "zip_filter"
    TARGZ_FILTER =  "targz_filter"
    JPG_FILTER =  "jpg_filter"
    DOCX_FILTER =  "docx_filter"
    APK_FILTER =  "apk_filter"
    ZOOPHILE_FILTER = "zoophile_filter"
    SENDER_CHAT_BLOCK = "sender_chat_block"
    SPOILER_BLOCK = "spoiler_block"
    SET_NO_VOCAL = "set_no_vocal"
    SET_ANTIFLOOD = "set_antiflood"
    BAN_MESSAGE = "ban_message"
    CREATED_AT = "created_at"
    UPDATED_AT = "updated_at"
    SET_GH = "set_gh"

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
    def add_with_dict(self,dictionary):
        placeholders = ', '.join(['%s'] * len(dictionary))
        columns = ', '.join(dictionary.keys())
        sql = "INSERT INTO groups ( %s ) VALUES ( %s )" % (columns, placeholders) # pylint: disable-this-line-in-some-way
        return self._dict_insert(sql, dictionary)

    #Update welcome buttons
    def updateWelcomeButtonsByGroupId(self, group_id, button):
        query = Query.update(groups).set(groups.welcome_buttons, '%s').where(groups.id_group == '%s')
        query = query.get_sql(quote_char='`')
        query = query.replace("'", "")

        self._update(query, [(button, group_id)])

    # I update the group id if the group changes from group to supergroup
    def update(self, args=None):
        q = "UPDATE groups SET id_group = %s WHERE id_group = %s"
        return self._update(q, args)

    # I insert the updates for the message count by group
    def insert_updates(self, args=None):
        q = "INSERT INTO nebula_updates (update_id, message_id, tg_group_id, tg_user_id, date) VALUES (%s,%s,%s,%s,%s)"
        return self._insert(q, args)

    # I collect the updates to know how many messages have been sent
    def getUpdatesByChatMonth(self, args=None):
        q = 'SELECT COUNT(*) AS counter FROM nebula_updates WHERE date BETWEEN DATE_SUB(NOW(), INTERVAL 31 DAY) AND NOW() AND tg_group_id = %s ORDER BY date DESC'

        return self._select(q, args)

    def getUpdatesByUserMonth(self, args=None):
        q = 'SELECT COUNT(*) AS counter FROM nebula_updates WHERE DATE BETWEEN DATE_SUB(NOW(), INTERVAL 30 DAY) AND NOW() AND tg_group_id = %s AND tg_user_id = %s ORDER BY DATE DESC'

        return self._select(q, args)

    def getAllUpdates(self):
        q = 'SELECT COUNT(*) AS counter FROM nebula_updates'

        return self._select(q)

    def change_group_photo(self, args=None):
        q = "INSERT INTO groups SET group_photo = %s WHERE id_group = %s"

        return self._insert(q, args)

    def get_group_badwords(self, args=None):
        q = "SELECT * FROM groups_badwords WHERE INSTR(%s, word) <> 0 AND tg_group_id = %s"

        return self._select(q, args)

    def get_antispam_logic(self, args=None):
        q = "SELECT * FROM nebula_antispam WHERE INSTR(%s, logic) <> 0"

        return self._select(q, args)

    def get_badwords_group(self, args=None):
        q = "SELECT * FROM groups_badwords WHERE tg_group_id = %s"

        return self._selectAll(q, args)

    def insert_badword(self, args=None):
        q = "INSERT IGNORE INTO groups_badwords (word, tg_group_id) VALUES (%s,%s)"

        return self._insert(q, args)

    def insert_spam(self, args=None):
        q = "INSERT IGNORE INTO nebula_antispam (logic) VALUES (%s)"

        return self._single_insert(q, args)


    def remove(self, args=None):
        q = "DELETE FROM groups WHERE id_group = %s"
        return self._delete(q, args)

    def get_custom_handler(self, args=None):
        q = "SELECT answer FROM custom_handler WHERE question = %s AND chat_id = %s"

        return self._select(q, args)

    def insert_custom_handler(self, args=None):
        q = "INSERT INTO custom_handler (chat_id, question, answer) VALUES (%s,%s,%s)"

        return self._insert(q, args)

    def getTopActiveUsers(self, args=None):

        q = "SELECT COUNT(*) AS counter, u.tg_username, u.tg_id FROM nebula_updates nu INNER JOIN users u ON u.tg_id = nu.tg_user_id WHERE DATE BETWEEN DATE_SUB(NOW(), INTERVAL 30 DAY) AND NOW() AND nu.tg_group_id = %s GROUP BY nu.tg_user_id ORDER BY counter DESC LIMIT 10"

        return self._selectAll(q, args)

    def getTopInactiveUsers(self, args=None):

        q = "SELECT COUNT(*) AS counter, u.tg_username, u.tg_id FROM nebula_updates nu INNER JOIN users u ON u.tg_id = nu.tg_user_id WHERE DATE BETWEEN DATE_SUB(NOW(), INTERVAL 30 DAY) AND NOW() AND nu.tg_group_id = %s GROUP BY nu.tg_user_id ORDER BY counter ASC LIMIT 10"

        return self._selectAll(q, args)

    ##########################
    ##### GROUP SETTINGS #####
    ##########################

    def set_block_entry(self, args=None):
        q = "UPDATE groups SET set_welcome = %s, block_new_member = %s WHERE id_group = %s"
        return self._update(q, args)

    def update_group_settings(self, record, args=None):
        q = "UPDATE groups SET @record = %s WHERE id_group = %s".replace('@record',record)
        return self._update(q, args)

    def job_nebula_updates(self, args=None):
        q = "DELETE FROM nebula_updates WHERE date < NOW() - INTERVAL 90 DAY"
        return self._delete(q, args)
