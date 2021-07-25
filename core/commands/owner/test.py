#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core import decorators
from config import Config

OWNERS_K = list(Config.OWNER.keys())
OWNERS_V = list(Config.OWNER.values())
@decorators.owner.init
def init(update,context):
    print("Gli Owners del bot sono:\n{} [{}]".format(OWNERS_K,OWNERS_V))