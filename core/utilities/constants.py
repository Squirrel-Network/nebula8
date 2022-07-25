#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from telegram import ChatPermissions

#general constants
DEFAULT_COUNT_WARN = 0
DEFAULT_USER_SCORE = 0
DEFAULT_MAX_WARN = 3
SERVICE_ACCOUNT = 777000

# constants for time management
# DAILY == 24h  ; TWELVE_HOUR == 12h ; EIGHT_HOUR == 8h ; FOUR_HOUR == 4h ; ONE_HOUR == 1h
DAILY = 86400.0
TWELVE_HOUR = 43200.0
EIGHT_HOUR = 28800.0
FOUR_HOUR = 14400.0
ONE_HOUR = 3600.0
ONE_MINUTE = 60.0

#these constants change and disrupt an entire group
PERM_FALSE = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages=False,
    can_send_polls=False,
    can_send_other_messages=False,
    can_add_web_page_previews=False,
    can_change_info=False,
    can_invite_users=False,
    can_pin_messages=False
    )
PERM_TRUE = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_polls=True,
    can_send_other_messages=True,
    can_add_web_page_previews=True,
    can_change_info=False,
    can_invite_users=False,
    can_pin_messages=False
    )

PERM_MEDIA_TRUE = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_polls=True,
    can_send_other_messages=True,
    can_add_web_page_previews=True,
    can_change_info=False,
    can_invite_users=False,
    can_pin_messages=False
    )

PERM_MEDIA_FALSE = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=False,
    can_send_polls=True,
    can_send_other_messages=False,
    can_add_web_page_previews=True,
    can_change_info=False,
    can_invite_users=False,
    can_pin_messages=False
    )