#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
import asyncio
from core.utilities.scheduler import Scheduler

job = Scheduler()
loop = asyncio.get_event_loop()

@job.repeat(10, True)
async def init():
    print("ciao")