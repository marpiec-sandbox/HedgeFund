# -*- coding: utf-8 -*-
import os

def ensureDirectoryForFile(fileName):
    directory = os.path.dirname(fileName)

    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError: pass #it looks like other thread have created it