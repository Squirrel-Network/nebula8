#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core import decorators
from core.utilities.functions import flag
from core.utilities.message import message


@decorators.owner.init
def init(update,context):
    print(update)
    a = flag('it')
    message(update,context,a)