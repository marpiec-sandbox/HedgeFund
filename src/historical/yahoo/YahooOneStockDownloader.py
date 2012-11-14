# -*- coding: utf-8 -*-
from string import Template
from Configuration import Configuration
from util import WebUtil

class YahooOneStockDownloader:

    _urlTemplate = Template('http://ichart.finance.yahoo.com/table.csv?s=${stockName}&a=00&b=1&c=2011&d=11&e=31&f=2011&g=d&ignore=.csv')
    _fileNameTemplate = Template(Configuration.HISTORICAL_DATA_DIR + "${exchangeName}/${stockName}.csv")

    def __init__(self, exchangeName, stockName):
        self._stockName = stockName
        self._url = self._urlTemplate.substitute(stockName = stockName)
        self._fileName = self._fileNameTemplate.substitute(exchangeName = exchangeName, stockName = stockName)


    def downloadHistoricalPrizes(self):
        WebUtil.downloadFromUrlAndSaveToFile(self._url, self._fileName, False)