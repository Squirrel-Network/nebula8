#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core import decorators


@decorators.owner.init
def init(update,context):
    print(update)