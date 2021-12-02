#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

import re

class Regex(object):
    HAS_ARABIC = "[\u0600-\u06ff]|[\u0750-\u077f]|[\ufb50-\ufbc1]|[\ufbd3-\ufd3f]|[\ufd50-\ufd8f]|[\ufd92-\ufdc7]|[\ufe70-\ufefc]|[\uFDF0-\uFDFD]+"
    HAS_CIRILLIC = "[а-яА-Я]+"
    HAS_CHINESE = "[\u4e00-\u9fff]+"
    HAS_NUMBER = "^[0-9]+$"
    HAS_LETTER = "^[a-zA-Z]+$"
    HAS_ZOOPHILE = "[ζ]"
    HAS_URL = "((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*"

    def check_string(regex_type,string):
        check = re.search(regex_type, string)
        if check is None:
            return False
        else:
            return True