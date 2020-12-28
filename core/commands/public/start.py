#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from languages.getLang import languages
from core.utilities.message import message
from core import decorators

@decorators.private.init
@decorators.delete.init
def init(update, context):
    languages(update,context)
    message(update,context,languages.start)