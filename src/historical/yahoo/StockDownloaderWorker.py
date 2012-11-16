# -*- coding: utf-8 -*-
from historical.yahoo.YahooOneStockDownloader import YahooOneStockDownloader

class StockDownloaderWorker:

    def __init__(self, exchangeName, fromDate, toDate):
        self._exchangeName = exchangeName
        self._fromDate = fromDate
        self._toDate = toDate

    def work(self, stockName):
        YahooOneStockDownloader(self._exchangeName, stockName, self._fromDate, self._toDate).downloadHistoricalPrizes()

