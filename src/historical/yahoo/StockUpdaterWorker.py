# -*- coding: utf-8 -*-
from historical.yahoo.YahooOneStockUpdater import YahooOneStockUpdater

class StockUpdaterWorker:

    def __init__(self, exchangeName, toDate):
        self._exchangeName = exchangeName
        self._toDate = toDate

    def work(self, stockName):
        YahooOneStockUpdater(self._exchangeName, stockName, self._toDate).updateHistoricalPrizes()