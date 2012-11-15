# -*- coding: utf-8 -*-
from historical.yahoo.YahooOneStockUpdater import YahooOneStockUpdater

class StockUpdaterWorker:

    def __init__(self, exchangeName, endDate):
        self._exchangeName = exchangeName
        self._endDate = endDate

    def work(self, stockName):
        YahooOneStockUpdater(self._exchangeName, stockName, self._endDate).updateHistoricalPrizes()