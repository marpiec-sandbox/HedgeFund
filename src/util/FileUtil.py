# -*- coding: utf-8 -*-
import os

def ensureDirectoryForFile(fileName):
    directory = os.path.dirname(fileName)
    if not os.path.exists(directory):
        os.makedirs(directory)