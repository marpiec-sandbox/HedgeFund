# -*- coding: utf-8 -*-
from datetime import date

import logging
import os
import time
import pylab
from optimizer.SharpeRatioOptimizer import SharpeRatioOptimizer
from statistics import statictics
from statistics.statictics import calculateSharpeRatioForStock

import numpy as np

from historical.HistoricalDataRetrieval import HistoricalDataRetrieval
from historical.StockListDownloader import StockListDownloader
from historical.yahoo.YahooDataDownloader import YahooDataDownloader
from historical.yahoo.YahooDataUpdater import YahooDataUpdater
from util.RemainingTimePrinter import RemainingTimePrinter


logging.basicConfig(level=logging.INFO)
start = time.clock()
#
##StockListDownloader("nyse").downloadAndConvertStockList()
#StockListDownloader("nasdaq").downloadAndConvertStockList()
#
##YahooDataDownloader("nyse").downloadStocks(date(2009, 1, 1), date.today())
#YahooDataDownloader("nasdaq").downloadStocks(date(2009, 1, 1), date.today())
#
##YahooDataUpdater("nyse").updateStocks(date.today())
#YahooDataUpdater("nasdaq").updateStocks(date.today())


exchangeName = "nasdaq"
stockNameA, stockNameB, proportion, sharpeRatio = SharpeRatioOptimizer().findBestStocksWithHighestSharpeRatio(exchangeName, date(2011, 1, 1), date(2011,12,31))

print "Best sharpe = " + str(sharpeRatio)+ " is for stock "+stockNameA + " and " + stockNameB + " with proportion 1:"+str(proportion)

end = time.clock()
print "All work took " + str(end - start) + " seconds."




stockDataRetrieval = HistoricalDataRetrieval(exchangeName)

stocksValuesA = np.array(stockDataRetrieval.loadAdjustedCloseValues(stockNameA, date(2011, 1, 1), date(2012,12,31)))
normalizedValuesA = stocksValuesA / stocksValuesA[0]
stocksValuesB = np.array(stockDataRetrieval.loadAdjustedCloseValues(stockNameB, date(2011, 1, 1), date(2012,12,31)))
normalizedValuesB = stocksValuesB / stocksValuesB[0]


pylab.plot(normalizedValuesA)
pylab.plot(normalizedValuesB)
pylab.plot((normalizedValuesA + normalizedValuesB * proportion) / (1 + proportion))
pylab.legend([stockNameA, stockNameB, "Portfolio"])
pylab.show()

