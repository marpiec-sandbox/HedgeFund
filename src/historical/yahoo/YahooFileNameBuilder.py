# -*- coding: utf-8 -*-
from string import Template
from Configuration import Configuration

class YahooFileNameBuilder:

    _fileNameTemplate = Template(Configuration.HISTORICAL_DATA_DIR + "${exchangeName}/${stockName}.csv")

    def __init__(self, exchangeName, stockName):
        self._fileName = self._fileNameTemplate.substitute(exchangeName = exchangeName, stockName = stockName)

    def build(self):
        return self._fileName
