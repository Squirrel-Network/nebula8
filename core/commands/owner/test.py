#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core import decorators
from config import Config

OWNERS = list(Config.OWNER.values())

@decorators.owner.init
def init(update,context):
    print(OWNERS)