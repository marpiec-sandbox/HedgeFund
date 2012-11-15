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
                with open(fileName, "w") as f:
                    lines = u.readlines()
                    f.write(lines[0])
                    f.writelines(reversed(lines[1:]))
                f.closed
            finally:
                u.close()
        except urllib2.HTTPError: logging.warning("Cannot load from: " + url)


def downloadFromUrlAndAppendToFile(url, fileName):
    if os.path.isfile(fileName):
        try:
            u = urllib2.urlopen(url)
            try:
                with open(fileName, "a") as f:
                    lines = u.readlines()
                    f.writelines(reversed(lines[1:]))
                f.closed
            finally:
                u.close()
        except urllib2.HTTPError: logging.warning("Cannot load from: " + url)