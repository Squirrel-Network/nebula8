#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core.utilities.scheduler import Scheduler

job = Scheduler()

@job.repeat(10, True)
async def init():
    print("ciao")