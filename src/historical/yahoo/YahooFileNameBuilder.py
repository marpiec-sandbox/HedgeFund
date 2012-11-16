# -*- coding: utf-8 -*-
from string import Template
from Configuration import Configuration

class YahooFileNameBuilder:

    def __init__(self, exchangeName):
        self._fileNameTemplate = Template(Configuration.HISTORICAL_DATA_DIR + exchangeName + "/${stockName}.csv")

    def build(self, stockName):
        return self._fileNameTemplate.substitute(stockName = stockName)
