#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core import decorators


@decorators.admin.user_admin
def init(update,context):
    print(update)