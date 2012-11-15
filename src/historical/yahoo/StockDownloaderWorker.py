# -*- coding: utf-8 -*-
from historical.yahoo.YahooOneStockDownloader import YahooOneStockDownloader

class StockDownloaderWorker:

    def __init__(self, exchangeName, startDate, endDate):
        self._exchangeName = exchangeName
        self._startDate = startDate
        self._endDate = endDate

    def work(self, stockName):
        YahooOneStockDownloader(self._exchangeName, stockName, self._startDate, self._endDate).downloadHistoricalPrizes()

