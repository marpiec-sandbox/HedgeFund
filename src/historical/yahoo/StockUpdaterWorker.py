# -*- coding: utf-8 -*-
from historical.yahoo.YahooOneStockUpdater import YahooOneStockUpdater

class StockUpdaterWorker:

    def __init__(self, exchangeName, startYear, startMonth, startDay, endYear, endMonth, endDay):
        self._exchangeName = exchangeName
        self._startYear = startYear
        self._startMonth = startMonth
        self._startDay = startDay
        self._endYear = endYear
        self._endMonth = endMonth
        self._endDay = endDay


    def work(self, stockName):
        YahooOneStockUpdater(self._exchangeName, stockName,
                self._startYear, self._startMonth, self._startDay,
            self._endYear, self._endMonth, self._endDay).updateHistoricalPrizes()