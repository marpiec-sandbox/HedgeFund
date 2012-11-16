# -*- coding: utf-8 -*-
from datetime import date

import logging
import os
import time
from analytics import analytics
from analytics.analytics import calculateSharpeRatioForStock

import numpy as np

from historical.HistoricalDataRetrieval import HistoricalDataRetrieval
from historical.StockListDownloader import StockListDownloader
from historical.yahoo.YahooDataDownloader import YahooDataDownloader
from historical.yahoo.YahooDataUpdater import YahooDataUpdater


logging.basicConfig(level=logging.INFO)
start = time.clock()

#StockListDownloader("nyse").downloadAndConvertStockList()
#StockListDownloader("nasdaq").downloadAndConvertStockList()

#YahooDataDownloader("nyse").downloadStocks(date(2009, 1, 1), date.today())
#YahooDataDownloader("nasdaq").downloadStocks(date(2009, 1, 1), date.today())

#YahooDataUpdater("nyse").updateStocks(date.today())
#YahooDataUpdater("nasdaq").updateStocks(date.today())

nasdaqDataRetrieval = HistoricalDataRetrieval("nasdaq")
nasdaqStocks = nasdaqDataRetrieval.getListOfStocks()
stocksLoaded = []

for a in range(len(nasdaqStocks)):
    if a % 100 == 0:
        print "Loading stocks...." + str(int(float(a)/float(len(nasdaqStocks))*100.0)) + "% done"
    stockName = nasdaqStocks[a]
    stocksLoaded.append(np.array(nasdaqDataRetrieval.loadAdjustedCloseValues(stockName, date(2011, 1, 1), date(2011, 12, 31)), np.float))

bestStockA = ""
bestStockB = ""
bestSharpe = 0.0

filteredStocks = []
for stock in stocksLoaded[:]:
    if stock[0] * 1.2 < stock[-1]:
        filteredStocks.append(stock)

stocksLoaded = filteredStocks

for a in range(len(stocksLoaded)):
    if a % 30 == 0:
        print "Calculating Sharpe...." + str(int(float(a)/float(len(stocksLoaded))*100.0)) + "% done"
    for b in range(len(stocksLoaded)):
        if a != b:
            stockA = stocksLoaded[a]
            stockB = stocksLoaded[b]
            if stockA.shape[0] == stockB.shape[0]:
                sharpeRatio = analytics.calculateSharpeRatioForStock(stockA + stockB)
                if sharpeRatio > bestSharpe:
                    bestStockA = nasdaqStocks[a]
                    bestStockB = nasdaqStocks[b]
                    bestSharpe = sharpeRatio


print "Best sharpe for " + bestStockA +" and " + bestStockB + " is " + str(bestSharpe)


end = time.clock()
print "All work took " + str(end - start) + " seconds."