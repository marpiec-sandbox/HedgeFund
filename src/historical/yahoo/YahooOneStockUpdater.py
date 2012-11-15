# -*- coding: utf-8 -*-
from string import Template
from Configuration import Configuration
from historical.yahoo.YahooFileNameBuilder import YahooFileNameBuilder
from historical.yahoo.YahooUrlBuilder import YahooUrlBuilder
from util import WebUtil

class YahooOneStockUpdater:

    def __init__(self, exchangeName, stockName, startDate, endDate):
        self._stockName = stockName
        self._url = YahooUrlBuilder(stockName, startDate, endDate).build()
        self._fileName = YahooFileNameBuilder(exchangeName, stockName).build()


    def updateHistoricalPrizes(self):
        WebUtil.downloadFromUrlAndAppendToFile(self._url, self._fileName)

