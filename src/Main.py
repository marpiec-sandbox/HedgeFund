# -*- coding: utf-8 -*-
from datetime import date

import logging
import os
import time
from historical.StockListDownloader import StockListDownloader
from historical.yahoo.YahooDataDownloader import YahooDataDownloader
from historical.yahoo.YahooDataUpdater import YahooDataUpdater

logging.basicConfig(level=logging.INFO)
start = time.clock()

#StockListDownloader("nyse").downloadAndConvertStockList()
#StockListDownloader("nasdaq").downloadAndConvertStockList()

#YahooDataDownloader("nyse").downloadStocks(date(2009, 1, 1), date.today())
#YahooDataDownloader("nasdaq").downloadStocks(date(2009, 1, 1), date.today())

YahooDataUpdater("nyse").updateStocks(date.today())
YahooDataUpdater("nasdaq").updateStocks(date.today())

end = time.clock()
print "All work took " + str(end - start) + " seconds."