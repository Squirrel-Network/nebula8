#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

import plugins
from telegram.ext import (CommandHandler as CMH)

def function_plugins(dsp):
    function = dsp.add_handler
    function(CMH('distro',plugins.distrowatch.init))
    function(CMH('google',plugins.search.google))
    function(CMH('mdn',plugins.search.mdn))
    function(CMH('ddg',plugins.search.duckduckgo))
    function(CMH('wiki',plugins.wikipedia.init))
    function(CMH('weather',plugins.weather.init))
    function(CMH('inspire',plugins.inspire.init))
    function(CMH('react',plugins.reactions.init))