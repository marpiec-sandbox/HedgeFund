# -*- coding: utf-8 -*-
import logging
import re
from string import Template
from Configuration import Configuration
from util import WebUtil, StringUtil

class StockListDownloader:

    _urlTemplate = Template("http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=${exchangeName}&render=download")
    _rawDataFileNameTemplate = Template(Configuration.HISTORICAL_DATA_DIR + "raw-data/${exchangeName}-rawlist.csv")
    _finalFileNameTemplate = Template(Configuration.HISTORICAL_DATA_DIR + "${exchangeName}-list.csv")

    def __init__(self, exchangeName):
        self._exchangeName = exchangeName
        self._url = self._urlTemplate.substitute(exchangeName = exchangeName)
        self._rawDataFileName = self._rawDataFileNameTemplate.substitute(exchangeName = exchangeName)
        self._finalFileName = self._finalFileNameTemplate.substitute(exchangeName = exchangeName)

    def downloadStockList(self):
        logging.info("Trying to download raw list of stocks from " + self._exchangeName)
        WebUtil.downloadFromUrlAndSaveToFile(self._url, self._rawDataFileName, False)
        logging.info("Downloaded raw list of stocks from " + self._exchangeName)

    def downloadAndConvertStockList(self):
        self.downloadStockList()
        self.convertListToProperFormat()

    def convertListToProperFormat(self):
        with open(self._rawDataFileName, 'r') as rawDataFile:
            with open(self._finalFileName, 'w') as finalFile:
                firstLineSkipped = False
                for rawDataLine in rawDataFile:
                    if firstLineSkipped:
                        self._convertLineToProperFormat(rawDataLine, finalFile)
                    else:
                        firstLineSkipped = True
            finalFile.closed
        rawDataFile.closed
        logging.info("Converted list of stocks from " + self._exchangeName)


    def _convertLineToProperFormat(self, rawDataLine, finalFile):
        try:
            foundGroups = re.search('"([A-Za-z\s\^/]+)"', rawDataLine)
            stockName = foundGroups.group(0)[1:-1].strip()
            if StringUtil.stringIsOnlyChars(stockName):
                finalFile.write(stockName + "\n")
        except AttributeError: logging.warn("Couldn't find a stock name in line: "+rawDataLine)



