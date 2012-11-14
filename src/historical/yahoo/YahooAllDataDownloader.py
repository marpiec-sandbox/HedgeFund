# -*- coding: utf-8 -*-
import logging
from util import WebUtil
from string import Template

from Configuration import Configuration
from historical.yahoo.YahooOneStockDownloader import YahooOneStockDownloader

class YahooAllDataDownloader:

    def __init__(self, exchangeName):
        self._exchangeName = exchangeName

    def downloadStocks(self):
        stockNameList = self._readStockList()
        logging.info("Loaded " + str(len(stockNameList)) + " stocks from file.")
        self._downloadHistoricalPrizesForStocks(stockNameList)

    def _readStockList(self):
        with open(Configuration.HISTORICAL_DATA_DIR + self._exchangeName + "-list.csv", 'r') as stockListFile:
            stockNameLines = stockListFile.readlines()
        stockListFile.closed

        stockNameList = []
        for stockNameLine in stockNameLines:
            stockNameList.append(stockNameLine[:-1])

        return stockNameList

    def _downloadHistoricalPrizesForStocks(self, stockNameList):
        stockCountString = str(len(stockNameList))
        counter = 1
        for stockName in stockNameList:
            YahooOneStockDownloader(self._exchangeName, stockName).downloadHistoricalPrizes()
            counter = counter + 1
            if counter % 100 == 0:
                print str(counter) + "/" + stockCountString

    

