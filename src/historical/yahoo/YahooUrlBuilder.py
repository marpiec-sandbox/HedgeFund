# -*- coding: utf-8 -*-
from datetime import date
from string import Template

class YahooUrlBuilder:

    _urlTemplate = Template("http://ichart.finance.yahoo.com/table.csv?" +
                            "s=${stockName}" +
                            "&a=${startZeroBasedMonth}&b=${startDay}&c=${startYear}" +
                            "&d=${endZeroBasedMonth}&e=${endDay}&f=${endYear}" +
                            "&g=d&ignore=.csv")

    def __init__(self, stockName, startDate, endDate):
        self._url = self._urlTemplate.substitute(stockName = stockName,
            startZeroBasedMonth = startDate.month - 1, startDay = startDate.day, startYear = startDate.year,
            endZeroBasedMonth = endDate.month - 1, endDay = endDate.day, endYear = endDate.year)

    def build(self):
        return self._url
