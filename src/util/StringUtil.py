# -*- coding: utf-8 -*-
import re

_onlyCharsRegexp = re.compile("^[A-Za-z]+$")

def stringIsOnlyChars(value):
    return _onlyCharsRegexp.match(value)

def formatDuration(timeInSeconds):
    seconds = timeInSeconds % 60
    rest = int(timeInSeconds) / 60
    minutes = rest % 60
    hours = int(rest) / 60
    formatted = ""
    if hours > 0:
        formatted = str(hours) + " hours "
    if minutes > 0:
        formatted = formatted + str(minutes) + " minutes "
    return formatted + ("%.1f" % seconds) + " seconds"