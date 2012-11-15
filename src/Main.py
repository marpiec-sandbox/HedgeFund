# -*- coding: utf-8 -*-

import logging
import time
from historical.StockListDownloader import StockListDownloader
from historical.yahoo.YahooAllDataDownloader import YahooAllDataDownloader
from historical.yahoo.YahooDataUpdater import YahooDataUpdater

logging.basicConfig(level=logging.INFO)
start = time.clock()

#StockListDownloader("nasdaq").downloadAndConvertStockList()
#StockListDownloader("nyse").downloadAndConvertStockList()

#YahooAllDataDownloader("nyse").downloadStocks()
#YahooAllDataDownloader("nasdaq").downloadStocks()

YahooDataUpdater("nyse").updateStocks()

end = time.clock()
print "All work took " + str(end - start) + " seconds."