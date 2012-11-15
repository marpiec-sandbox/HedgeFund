# -*- coding: utf-8 -*-
import os
from Configuration import Configuration
from historical.yahoo.StockDownloaderWorker import StockDownloaderWorker
from historical.yahoo.StockUpdaterWorker import StockUpdaterWorker
from util.threads.ThreadPoolManager import ThreadPoolManager


class YahooDataUpdater:

    def __init__(self, exchangeName):
        self._exchangeName = exchangeName

    def updateStocks(self, endDate):
        stockNameList = self._readStockList()
        self._updateStockData(stockNameList, endDate)

    def _readStockList(self):
        stockFiles = os.listdir(Configuration.HISTORICAL_DATA_DIR + self._exchangeName)
        stockNameList = []
        for stockFile in stockFiles:
            stockName = self._extractStockName(stockFile)
            stockNameList.append(stockName)
        return stockNameList
            
            
    def _extractStockName(self, stockFile):
        return stockFile[:-4]

    def _updateStockData(self, stockNameList, endDate):
        threadPool = ThreadPoolManager(Configuration.DEFAULT_WORKER_THREADS_COUNT)
        threadPool.addTasks(stockNameList)
        threadPool.startWork(StockUpdaterWorker(self._exchangeName, endDate))