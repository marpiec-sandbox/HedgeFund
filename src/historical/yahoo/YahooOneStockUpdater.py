# -*- coding: utf-8 -*-
from datetime import date, timedelta
import os
import re
from historical.yahoo.YahooFileNameBuilder import YahooFileNameBuilder
from historical.yahoo.YahooUrlBuilder import YahooUrlBuilder
from util import WebUtil

class YahooOneStockUpdater:
    MAXIMUM_FILE_LINE_LENGTH = 100

    def __init__(self, exchangeName, stockName, endDate):
        self._stockName = stockName
        self._endDate = endDate
        self._fileName = YahooFileNameBuilder(exchangeName, stockName).build()


    def updateHistoricalPrizes(self):
        startDate = self._getStartDateForStock()
        if startDate < self._endDate:
            self._url = YahooUrlBuilder(self._stockName, startDate, self._endDate).build()
            WebUtil.downloadFromUrlAndAppendToFile(self._url, self._fileName)

    def _getStartDateForStock(self):
        lastLine = self._getLastLineInFile()
        lastDate = self._parseLineToFindTheDate(lastLine)
        theDayAfter = self._calculateTheDayAfter(lastDate)
        return theDayAfter

    def _getLastLineInFile(self):
        fileSize = os.path.getsize(self._fileName)
        with open(self._fileName, "r") as f:
            f.seek(fileSize - self.MAXIMUM_FILE_LINE_LENGTH)
            lastLine = f.readlines()[-1]
        f.closed
        return lastLine


    def _parseLineToFindTheDate(self, line):
        foundDate = re.search("[0-9]+\-[0-9]+\-[0-9]+", line).group(0)
        dateArray = foundDate.split("-")
        return date(int(dateArray[0]), int(dateArray[1]), int(dateArray[2]))

    def _calculateTheDayAfter(self, someDate):
        return someDate + timedelta(days=1)