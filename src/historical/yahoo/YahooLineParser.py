# -*- coding: utf-8 -*-

# Date,Open,High,Low,Close,Volume,Adj Close
# 2009-01-02,15.60,16.30,15.51,16.24,3030200,16.12

from datetime import date

class YahooLineParser:

    def __init__(self, line):
        self._parseLine(line)

    def _parseLine(self, line):
        splitted = line.split(",")
        self.date = self._parseDate(splitted[0])
        self.open = float(splitted[1])
        self.high = float(splitted[2])
        self.low = float(splitted[3])
        self.close = float(splitted[4])
        self.volume = int(splitted[5])
        self.adjustedClose = float(splitted[6])

    def _parseDate(self, dateText):
        splitted = dateText.split("-")
        return date(int(splitted[0]), int(splitted[1]), int(splitted[2]))
