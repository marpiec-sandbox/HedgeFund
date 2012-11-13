# -*- coding: utf-8 -*-
from Configuration import Configuration
from util import WebUtil

class StockListDownloader:

    def downloadStockList(self):
        WebUtil.downloadFromUrlAndSaveToFile("http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download",
        Configuration.HISTORICAL_DATA_DIR + "temp/nasdaq.csv", False)
