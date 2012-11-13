# -*- coding: utf-8 -*-
import logging
import os
from string import Template
import urllib2

from Configuration import Configuration

class HistoricalDataDownloader:

    def __init__(self, exchangeName):
        self._exchangeName = exchangeName
        self._urlTemplate = Template('http://ichart.finance.yahoo.com/table.csv?s=${stockName}&a=00&b=1&c=2011&d=11&e=31&f=2011&g=d&ignore=.csv')
        self._fileNameTemplate = Template(Configuration.HISTORICAL_DATA_DIR + self._exchangeName + "/${stockName}.csv")

    def downloadStocks(self):
        stockNameList = self._readStockList()
        logging.info("Loaded " + str(len(stockNameList)) + " stocks from file.")
        self.downloadHistoricalPrizesForStocks(stockNameList)

    def _readStockList(self):
        with open(Configuration.HISTORICAL_DATA_DIR + self._exchangeName + "-list.csv", 'r') as stockListFile:
            stockNameLines = stockListFile.readlines()
        stockListFile.closed

        stockNameList = []
        for stockNameLine in stockNameLines:
            stockNameList.append(stockNameLine[:-1])

        return stockNameList

    def downloadHistoricalPrizesForStocks(self, stockNameList):
        stockCountString = str(len(stockNameList))
        counter = 1
        for stockName in stockNameList:
            self.downloadHistoricalPrizes(stockName)
            counter = counter + 1
            if counter % 100 == 0:
                print str(counter) + "/" + stockCountString

    def downloadHistoricalPrizes(self, stockName):
        url = self._urlTemplate.substitute(stockName = stockName)
        fileName = self._fileNameTemplate.substitute(stockName = stockName)
        self.downloadFileFromUrlAndWriteIt(url, fileName)

    def downloadFileFromUrlAndWriteIt(self, url, fileName):
        if not os.path.isfile(fileName):
            try:
                u = urllib2.urlopen(url)
                with open(fileName, "w") as file:
                    file.write(u.read())
                file.closed
            except urllib2.HTTPError: logging.warning("Cannot load from: "+url)
