#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
import asyncio
from core import decorators
from core.utilities.message import messageWithAsync

loop = asyncio.get_event_loop()

@decorators.owner.init
def init(update,context):
      loop.run_until_complete(messageWithAsync(update,context,1,"ASYNC TEST"))