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
        stockFiles = os.listdir(stocksDir)
        for stockFileName in stockFiles:
            stockList.append(stockFileName[:-4])
        return sorted(stockList)

    def getListOfStocks(self):
        return self._stockList

    def loadAdjustedCloseValues(self, stockName, fromDate, toDate):
        loadedValues = []
        with open(self._fileNameBuilder.build(stockName)) as f:
            f.readline() #skip headers
            line = self._findDateInFile(f, fromDate)
            while line:
                lineParser = YahooLineParser(line)
                lineDate = lineParser.date
                if fromDate <= lineDate <= toDate:
                    loadedValues.append(lineParser.adjustedClose)
                    line = f.readline()
                elif lineDate > toDate:
                    break
        return loadedValues

    def _findDateInFile(self, f, expectedDate):

        fileSize = os.path.getsize(f.name)
        line = f.readline()
        currentLineDate = YahooLineParser(line).date  #read first date in file

        dayDifference = (expectedDate - currentLineDate).days

        if dayDifference > 0:  # if first day in file is before expected date
            estimatedLineLength = len(line)
            maximumFileCursorPosition = fileSize - int(estimatedLineLength*1.5)

            while dayDifference > 5 or dayDifference < 1:  #we are looking for some days near and before expectedDate
                estimatedDayDifference = dayDifference * 5 / 7 # estimated day difference in working days
                if estimatedDayDifference <= 0:
                    dayFileJump = min(estimatedDayDifference, -3) #jump at least 3 lines back
                else:
                    dayFileJump = estimatedDayDifference
                newFileCursorPosition = f.tell() + dayFileJump * estimatedLineLength
                if newFileCursorPosition > maximumFileCursorPosition: #if we jump to the end of file or further we'll check the last date in file
                    newFileCursorPosition = maximumFileCursorPosition
                    f.seek(newFileCursorPosition)
                    f.readline() #skip possibly not complete line
                    line = f.readline()
                    currentLineDate = YahooLineParser(line).date
                    if currentLineDate < expectedDate:# if last date in file is before expected day we end seeking and returning false
                        return False
                f.seek(newFileCursorPosition)
                f.readline() #skip possibly not complete line
                line = f.readline()
                currentLineDate = YahooLineParser(line).date
                dayDifference = (expectedDate - currentLineDate).days

            while currentLineDate < expectedDate: #now we are few days before expected date so just read every line until dates are equal
                line = f.readline()
                lineParser = YahooLineParser(line)
                currentLineDate = lineParser.date
        return line