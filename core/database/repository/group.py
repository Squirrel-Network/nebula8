#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core.database.db_connect import Connection
from pypika import Query, Table
from config import Config

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
    SET_COMMUNITY = "community"
    SET_WELCOME_TEXT = "welcome_text"
    SET_LOG_CHANNEL = "log_channel"
    SET_MAX_WARN = "max_warn"
    SET_CAS_BAN = "set_cas_ban"
    SET_TPNU = "type_no_username"
    SET_GROUP_PHOTO = "group_photo"
    SET_GROUP_MEMBERS_COUNT = "total_users"
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
    def add(self,args=None):
        q = "INSERT INTO groups (id_group, group_name, welcome_text, welcome_buttons, rules_text, community, languages, set_welcome, max_warn, set_silence, exe_filter, block_new_member, set_arabic_filter, set_cirillic_filter, set_chinese_filter, set_user_profile_picture, gif_filter, set_cas_ban, type_no_username, log_channel, group_photo, total_users) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        return self._insert(q, args)

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

    def insert_updates(self, args=None):
        q = "INSERT INTO nebula_updates (update_id, tg_group_id, date) VALUES (%s,%s,%s)"
        return self._insert(q, args)

    def getUpdatesByChat(self, args=None):
        q = 'SELECT COUNT(*) AS counter FROM nebula_updates WHERE tg_group_id = %s'

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

    ##########################
    ##### GROUP SETTINGS #####
    ##########################

    def set_block_entry(self, args=None):
        q = "UPDATE groups SET set_welcome = %s, block_new_member = %s WHERE id_group = %s"
        return self._update(q, args)

    def update_group_settings(self, record, args=None):
        q = "UPDATE groups SET @record = %s WHERE id_group = %s".replace('@record',record)
        return self._update(q, args)
