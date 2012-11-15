# -*- coding: utf-8 -*-
import contextlib
import logging
import os
import urllib2
from util import FileUtil

def downloadFromUrlAndSaveToFile(url, fileName, skipIfFileExists):
    if not(skipIfFileExists or os.path.isfile(fileName)):
        try:
            u = urllib2.urlopen(url)
            try:
                FileUtil.ensureDirectoryForFile(fileName)
                with open(fileName, "wb") as f:
                    f.write(u.read())
                f.closed
            finally:
                u.close()
        except urllib2.HTTPError: logging.warning("Cannot load from: " + url)
