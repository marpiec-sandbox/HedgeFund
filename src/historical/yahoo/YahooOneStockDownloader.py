# -*- coding: utf-8 -*-
from historical.yahoo.YahooFileNameBuilder import YahooFileNameBuilder
from historical.yahoo.YahooUrlBuilder import YahooUrlBuilder
from util import WebUtil

class YahooOneStockDownloader:
    def __init__(self, exchangeName, stockName, fromDate, toDate):
        self._stockName = stockName
        self._url = YahooUrlBuilder(stockName, fromDate, toDate).build()
        self._fileName = YahooFileNameBuilder(exchangeName).build(stockName)


    def downloadHistoricalPrizes(self):
        WebUtil.downloadFromUrlAndSaveToFile(self._url, self._fileName, False)