# -*- coding: utf-8 -*-

import logging
import time
from historical.StockListDownloader import StockListDownloader
from historical.yahoo.YahooAllDataDownloader import YahooAllDataDownloader

logging.basicConfig(level=logging.INFO)
start = time.clock()

#StockListDownloader("nasdaq").downloadAndConvertStockList()
#StockListDownloader("nyse").downloadAndConvertStockList()

YahooAllDataDownloader("nyse").downloadStocks()
YahooAllDataDownloader("nasdaq").downloadStocks()


end = time.clock()
print "All work took " + str(end - start) + " seconds."