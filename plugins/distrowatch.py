#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

import requests
from core import decorators
from bs4 import BeautifulSoup
from core.utilities.message import message

@decorators.delete.init
def init(update, context):
    r = requests.get("https://distrowatch.com/random.php")
    parsed_html = BeautifulSoup(r.text, features="html.parser")
    distro_long_name = parsed_html.title.string[17:].lower()
    distro_name = distro_long_name.split()[0]
    distro_url = f'https://distrowatch.com/table.php?distribution={distro_name}'
    distro_message = "Here is a random linux distribution: {}".format(distro_url)
    message(update,context,distro_message)