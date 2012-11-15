# -*- coding: utf-8 -*-
import logging
from multiprocessing.pool import ThreadPool
from historical.yahoo.StockDownloaderWorker import StockDownloaderWorker
from util import WebUtil
from string import Template

from Configuration import Configuration
from historical.yahoo.YahooOneStockDownloader import YahooOneStockDownloader
from util.threads.ThreadPoolManager import ThreadPoolManager

class YahooDataDownloader:

    def __init__(self, exchangeName):
        self._exchangeName = exchangeName

    def downloadStocks(self, startDate, endDate):
        stockNameList = self._readStockList()
        logging.info("Loaded " + str(len(stockNameList)) + " stocks from file.")
        self._downloadHistoricalPrizesForStocks(stockNameList, startDate, endDate)

    def _readStockList(self):
        with open(Configuration.HISTORICAL_DATA_DIR + self._exchangeName + "-list.csv", 'r') as stockListFile:
            stockNameLines = stockListFile.readlines()
        stockListFile.closed

        stockNameList = []
        for stockNameLine in stockNameLines:
            stockNameList.append(stockNameLine[:-1])

        return stockNameList

    def _downloadHistoricalPrizesForStocks(self, stockNameList, startDate, endDate):

#        for stockName in stockNameList:
#            YahooOneStockDownloader(self._exchangeName, stockName).downloadHistoricalPrizes()

        threadPool = ThreadPoolManager(Configuration.DEFAULT_WORKER_THREADS_COUNT)
        threadPool.addTasks(stockNameList)
        threadPool.startWork(StockDownloaderWorker(self._exchangeName, startDate, endDate))
