# -*- coding: utf-8 -*-
from datetime import date

import logging
import time
from historical.StockListDownloader import StockListDownloader
from historical.yahoo.YahooDataDownloader import YahooDataDownloader
from historical.yahoo.YahooDataUpdater import YahooDataUpdater

logging.basicConfig(level=logging.INFO)
start = time.clock()

#StockListDownloader("nyse").downloadAndConvertStockList()
#StockListDownloader("nasdaq").downloadAndConvertStockList()


#YahooDataDownloader("nyse").downloadStocks(date(2011, 1, 1), date(2011, 12, 31))
#YahooDataDownloader("nasdaq").downloadStocks(date(2011, 1, 1), date(2011, 12, 31))

YahooDataUpdater("nyse").updateStocks(date(2012, 1, 1), date(2012, 3, 31))

end = time.clock()
print "All work took " + str(end - start) + " seconds."