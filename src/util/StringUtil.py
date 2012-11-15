# -*- coding: utf-8 -*-
import re

_onlyCharsRegexp = re.compile("^[A-Za-z]+$")

def stringIsOnlyChars(value):
    return _onlyCharsRegexp.match(value)