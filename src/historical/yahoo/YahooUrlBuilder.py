# -*- coding: utf-8 -*-
from datetime import date
from string import Template

class YahooUrlBuilder:

    _urlTemplate = Template("http://ichart.finance.yahoo.com/table.csv?" +
                            "s=${stockName}" +
                            "&a=${startZeroBasedMonth}&b=${startDay}&c=${startYear}" +
                            "&d=${endZeroBasedMonth}&e=${endDay}&f=${endYear}" +
                            "&g=d&ignore=.csv")

    def __init__(self, stockName, fromDate, toDate):
        self._url = self._urlTemplate.substitute(stockName = stockName,
            startZeroBasedMonth = fromDate.month - 1, startDay = fromDate.day, startYear = fromDate.year,
            endZeroBasedMonth = toDate.month - 1, endDay = toDate.day, endYear = toDate.year)

    def build(self):
        return self._url
