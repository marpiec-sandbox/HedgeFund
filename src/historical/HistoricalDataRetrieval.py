# -*- coding: utf-8 -*-
import os
from Configuration import Configuration
from historical.yahoo.YahooFileNameBuilder import YahooFileNameBuilder
from historical.yahoo.YahooLineParser import YahooLineParser

class HistoricalDataRetrieval:

    def __init__(self, exchangeName):
        self._exchangeName = exchangeName
        self._stocksDir = Configuration.HISTORICAL_DATA_DIR + self._exchangeName
        self._stockList = self._loadListOfStocks(self._stocksDir)
        self._fileNameBuilder = YahooFileNameBuilder(self._exchangeName)
        pass

    def _loadListOfStocks(self, stocksDir):
        stockList = []
        stockFiles = os.listdir(self._stocksDir)
        for stockFileName in stockFiles:
            stockList.append(stockFileName[:-4])
        return sorted(stockList)

    def getListOfStocks(self):
        return self._stockList

    def loadAdjustedCloseValues(self, stockName, fromDate, toDate):
        loadedValues = []
        with open(self._fileNameBuilder.build(stockName)) as f:
            firstLineSkipped = False
            for line in f:
                if firstLineSkipped:

                    lineParser = YahooLineParser(line)
                    lineDate = lineParser.date
                    if lineDate >= fromDate and lineDate <= toDate:
                        loadedValues.append(lineParser.adjustedClose)
                else:
                    firstLineSkipped = True

        return loadedValues


