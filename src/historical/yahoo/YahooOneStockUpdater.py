# -*- coding: utf-8 -*-
from string import Template
from Configuration import Configuration
from util import WebUtil

class YahooOneStockUpdater:

    _urlTemplate = Template("http://ichart.finance.yahoo.com/table.csv?" +
                            "s=${stockName}" +
                            "&a=${startZeroBasedMonth}&b=${startDay}&c=${startYear}" +
                            "&d=${endZeroBasedMonth}&e=${endDay}&f=${endYear}" +
                            "&g=d&ignore=.csv")
    _fileNameTemplate = Template(Configuration.HISTORICAL_DATA_DIR + "${exchangeName}/${stockName}.csv")

    def __init__(self, exchangeName, stockName, startYear, startMonth, startDay, endYear, endMonth, endDay):
        self._stockName = stockName
        self._url = self._urlTemplate.substitute(stockName = stockName,
            startZeroBasedMonth = startMonth - 1, startDay = startDay, startYear = startYear,
            endZeroBasedMonth = endMonth - 1, endDay = endDay, endYear = endYear)
        self._fileName = self._fileNameTemplate.substitute(exchangeName = exchangeName, stockName = stockName)


    def updateHistoricalPrizes(self):
        WebUtil.downloadFromUrlAndAppendToFile(self._url, self._fileName)

