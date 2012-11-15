# -*- coding: utf-8 -*-
from historical.yahoo.YahooOneStockUpdater import YahooOneStockUpdater

class StockUpdaterWorker:

    def __init__(self, exchangeName, startDate, endDate):
        self._exchangeName = exchangeName
        self._startDate = startDate
        self._endDate = endDate

    def work(self, stockName):
        YahooOneStockUpdater(self._exchangeName, stockName, self._startDate, self._endDate).updateHistoricalPrizes()