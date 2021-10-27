#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core import decorators
from core.database.db_connect import Connection


@decorators.owner.init
def init(update,context):
    a = Connection()
    if a:
        print("OH SI OH SI ANCORA SPINGILO TUTTO")
    else:
        print("MORIREMO TUTTI!")