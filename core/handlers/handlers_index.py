#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
import rx
from telegram import update
from core import handlers
from core.commands import public
from rx.subject import Subject
from rx.core import Observable
from rx import operators as ops
from telegram.ext import (MessageHandler as MH,Filters)

def tap(fn):
    def _tap(source):
        def subscribe(obv, scheduler = None):
            def on_next(value):
                try:
                    fn(value)
                except Exception as err:  # pylint: disable=broad-except
                    obv.on_error(err)
                else:
                    obv.on_next(value)
            return source.subscribe_(on_next, obv.on_error, obv.on_completed, scheduler)
        return Observable(subscribe)
    return _tap

def build_event(event_type, update, context):
    return { 'event_type': event_type, 'update': update, 'context': context }

def new_chat_members(update, context):
    handlers.welcome.init(update, context)

    return rx.just([update, context])

def chat_type(update, context):
    handlers.check_status_user.check_status(update, context)
    handlers.check_status_chat.check_status(update, context)
    public.report.init(update,context)
    handlers.filters_chat.init(update, context)
    handlers.logs.set_log_channel(update,context)

    return rx.just([update, context])

def core_handlers(dsp):
    handler = Subject()

    handler_next = lambda event_type : lambda *args : handler.on_next(build_event(event_type, *args))
    is_same_event = lambda event_type : lambda event_mapping: event_mapping['name'] == event_type['name']

    event_mappings = [
        { 'name': 'new_chat_members', 'filter': Filters.status_update.new_chat_members, 'fn': new_chat_members },
        { 'name': 'chat_type', 'filter': Filters.chat_type, 'fn': chat_type }
    ]

    for event_type in event_mappings:
        dsp.add_handler(MH(event_type['filter'], handler_next(event_type), run_async=True))

    handler.pipe(
        ops.flat_map(
            lambda event_type, args :
                rx.just(event_mappings
                    .filter(is_same_event(event_type))
                    .map(lambda event_type: event_type['fn'](*args)))
        )
    ).subscribe(lambda *v : print(v))
    #.pipe(tap(lambda value : log(value)))