#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

import asyncio
from time import time
from typing import Callable, List, Dict, Any

"""
=============
How to Use:
=============
test = Scheduler()

@test.repeat(3600, False)
async def handler():
  It will be repeated at 16:30
  It will be repeated at 17:30
  It will be repeated at 18:30

OR...

@test.repeat(3600, True)
async def handler():
  It will be repeated at 16:00
  It will be repeated at 17:00
  It will be repeated at 18:00

"""

class Scheduler:
    def __init__(self):
        self._schedule_list: List[Dict[str, Any]] = []

    def repeat(self, delay_seconds: int, use_system_time: bool = False) -> Callable:
        def decorator(func: Callable) -> Callable:
            if self is not None:
                self._schedule_list.append({
                    'time': delay_seconds,
                    'repeated': True,
                    'callable': func,
                    'system_time': use_system_time,
                    'last_call': self._system_time(delay_seconds)
                    if use_system_time else time(),
                })
            return func
        return decorator

    def delay(self, delay_seconds: int, use_system_time: bool = False) -> Callable:
        def decorator(func: Callable) -> Callable:
            if self is not None:
                self._schedule_list.append({
                    'time': delay_seconds,
                    'repeated': False,
                    'callable': func,
                    'system_time': use_system_time,
                    'last_call': self._system_time(delay_seconds)
                    if use_system_time else time(),
                })
            return func
        return decorator

    @staticmethod
    def _system_time(divided_by: int) -> int:
        return int(int(time()) / divided_by) * divided_by

    def start(self):
        async def core_runner():
            async def clock():
                while True:
                    curr_time = time()
                    for item in self._schedule_list:
                        if curr_time - item['last_call'] >= item['time']:
                            if item['system_time']:
                                curr_time = self._system_time(item['time'])
                            item['last_call'] = curr_time
                            asyncio.ensure_future(item['callable']())
                            if not item['repeated']:
                                self._schedule_list.remove(item)
                    await asyncio.sleep(1)

            asyncio.ensure_future(clock())
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(core_runner())
        except KeyboardInterrupt:
            pass
