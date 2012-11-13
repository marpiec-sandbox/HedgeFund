# -*- coding: utf-8 -*-
import logging
import os
import urllib2
from util import FileUtil

def downloadFromUrlAndSaveToFile(url, fileName, skipIfFileExists):
    FileUtil.ensureDirectoryForFile(fileName)
    if not(skipIfFileExists or os.path.isfile(fileName)):
        try:
            u = urllib2.urlopen(url)
            with open(fileName, "wb") as file:
                file.write(u.read())
            file.closed
        except urllib2.HTTPError: logging.warning("Cannot load from: " + url)
