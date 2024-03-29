#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

class Migrations(object):
    USERS = 'CREATE TABLE IF NOT EXISTS nebula.users (id int(11) NOT NULL,tg_id varchar(50) NOT NULL,tg_username varchar(50) NOT NULL,created_at datetime NOT NULL,updated_at datetime NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4'
    OWNERS = 'CREATE TABLE IF NOT EXISTS nebula.owner_list (id int(11) NOT NULL,tg_id varchar(255) NOT NULL,tg_username varchar(255) NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4'
    GROUPS = "CREATE TABLE IF NOT EXISTS nebula.groups (" \
            "id int(11) NOT NULL AUTO_INCREMENT," \
            "id_group varchar(50) NOT NULL," \
            "group_name varchar(255) NOT NULL," \
            "welcome_text text NOT NULL," \
            "welcome_buttons longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL DEFAULT '{}'," \
            "rules_text text NOT NULL," \
            "community tinyint(1) NOT NULL DEFAULT 0," \
            "languages varchar(20) DEFAULT 'EN'," \
            "set_welcome tinyint(2) NOT NULL DEFAULT 1," \
            "max_warn int(11) NOT NULL DEFAULT 3," \
            "set_silence tinyint(2) NOT NULL DEFAULT 0," \
            "exe_filter tinyint(1) NOT NULL DEFAULT 0," \
            "block_new_member tinyint(1) NOT NULL DEFAULT 0," \
            "set_arabic_filter tinyint(1) NOT NULL DEFAULT 1," \
            "set_cirillic_filter tinyint(1) NOT NULL DEFAULT 1," \
            "set_chinese_filter tinyint(1) NOT NULL DEFAULT 1," \
            "set_user_profile_picture tinyint(1) NOT NULL DEFAULT 0," \
            "gif_filter tinyint(1) NOT NULL DEFAULT 0," \
            "set_cas_ban tinyint(1) NOT NULL DEFAULT 1," \
            "type_no_username int(1) NOT NULL DEFAULT 1," \
            "log_channel varchar(50) NOT NULL DEFAULT '-1001359708474'," \
            "group_photo varchar(255) NOT NULL DEFAULT 'https://naos.hersel.it/group_photo/default.jpg'," \
            "total_users int(50) NOT NULL DEFAULT 0," \
            "zip_filter tinyint(1) NOT NULL DEFAULT 0," \
            "targz_filter tinyint(1) NOT NULL DEFAULT 0," \
            "jpg_filter tinyint(1) NOT NULL DEFAULT 0," \
            "docx_filter tinyint(1) NOT NULL DEFAULT 0," \
            "apk_filter tinyint(1) NOT NULL DEFAULT 0," \
            "zoophile_filter tinyint(1) NOT NULL DEFAULT 1," \
            "sender_chat_block tinyint(1) NOT NULL DEFAULT 1," \
            "spoiler_block tinyint(1) NOT NULL DEFAULT 0," \
            "set_no_vocal tinyint(1) NOT NULL DEFAULT 0," \
            "set_antiflood tinyint(1) NOT NULL DEFAULT 1," \
            "ban_message text NOT NULL DEFAULT '{mention} has been banned from: {chat}'",\
            "PRIMARY KEY (id)," \
            "UNIQUE KEY group_id (id_group)" \
            ") ENGINE=InnoDB AUTO_INCREMENT=141 DEFAULT CHARSET=utf8mb4".format('{  "buttons": [{"id": 0,"title": "Bot Logs","url": "https://t.me/nebulalogs"}]}')
    COMMUNITY = "CREATE TABLE IF NOT EXISTS nebula.community (id int(11) NOT NULL,tg_group_name varchar(50) DEFAULT NULL,tg_group_id varchar(50) DEFAULT NULL,tg_group_link varchar(50) DEFAULT NULL,language varchar(50) NOT NULL DEFAULT 'IT',type varchar(50) NOT NULL DEFAULT 'supergroup') ENGINE=InnoDB DEFAULT CHARSET=utf8mb4"
    GROUPS_BADWORDS = "CREATE TABLE IF NOT EXISTS nebula.groups_badwords (id int(11) NOT NULL,word varchar(255) NOT NULL,tg_group_id varchar(255) NOT NULL,user_score bigint(20) NOT NULL DEFAULT 0) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4"
    GROUP_USERS = "CREATE TABLE IF NOT EXISTS nebula.group_users (id int(11) NOT NULL,tg_id varchar(50) DEFAULT NULL,tg_group_id varchar(50) DEFAULT NULL,warn_count int(11) NOT NULL DEFAULT 0) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4"
    NEBULA_UPDATES = "CREATE TABLE IF NOT EXISTS nebula.nebula_updates (id int(11) NOT NULL AUTO_INCREMENT,update_id varchar(255) NOT NULL,tg_group_id varchar(255) NOT NULL,tg_user_id varchar(255) NOT NULL,date datetime(6) NOT NULL,PRIMARY KEY (id),UNIQUE KEY update_index (update_id)) ENGINE=InnoDB AUTO_INCREMENT=184434 DEFAULT CHARSET=utf8mb4"