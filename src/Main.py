# -*- coding: utf-8 -*-
from datetime import date

import logging
import os
import time
import pylab
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

#StockListDownloader("nyse").downloadAndConvertStockList()
#StockListDownloader("nasdaq").downloadAndConvertStockList()

#YahooDataDownloader("nyse").downloadStocks(date(2009, 1, 1), date.today())
#YahooDataDownloader("nasdaq").downloadStocks(date(2009, 1, 1), date.today())

#YahooDataUpdater("nyse").updateStocks(date.today())
#YahooDataUpdater("nasdaq").updateStocks(date.today())

nasdaqDataRetrieval = HistoricalDataRetrieval("nasdaq")
nasdaqStocksNames = nasdaqDataRetrieval.getListOfStocks()
normalizedStocks = []

timePrinter = RemainingTimePrinter(len(nasdaqStocksNames))

for a in range(len(nasdaqStocksNames)):
    timePrinter.printMessage(a)
    stockName = nasdaqStocksNames[a]
    stockArray = np.array(nasdaqDataRetrieval.loadAdjustedCloseValues(stockName, date(2011, 1, 1), date(2011,12,31)), np.float)
    if stockArray.shape[0] > 100:
        normalizedStock = stockArray / stockArray[0]
        normalizedStocks.append(normalizedStock)

timePrinter.printLastMessage()

bestA = -1
bestB = -1
bestC = -1
bestD = -1
bestStockA = ""
bestStockB = ""
bestStockC = ""
bestStockD = ""
bestSharpe = 0.0

filteredStocks = []
for stock in normalizedStocks[:]:
    if stock[0] * 1.6 < stock[-1]:
        filteredStocks.append(stock)

print "Stock count = " + str(len(filteredStocks))

normalizedStocks = filteredStocks

timePrinter = RemainingTimePrinter(len(normalizedStocks)*len(normalizedStocks)*len(normalizedStocks))
for a in range(len(normalizedStocks)):
    for b in range(len(normalizedStocks)):
        for c in range(len(normalizedStocks)):
            timePrinter.printMessage(c + b * len(normalizedStocks) + a * len(normalizedStocks) * len(normalizedStocks))
            if a != b and a != c and b != c:
                stockA = normalizedStocks[a]
                stockB = normalizedStocks[b]
                stockC = normalizedStocks[c]
                if stockA.shape[0] == stockB.shape[0] and stockA.shape[0] == stockC.shape[0]:
                    sharpeRatio = statictics.calculateSharpeRatioForStock(stockA + stockB + stockC)
                    if sharpeRatio > bestSharpe:
                        bestStockA = nasdaqStocksNames[a]
                        bestStockB = nasdaqStocksNames[b]
                        bestStockC = nasdaqStocksNames[c]
                        bestSharpe = sharpeRatio
                        bestA = a
                        bestB = b
                        bestC = c

timePrinter.printLastMessage()


#print str(bestA) + " " + str(bestB) + " " + str(normalizedStocks[bestA][0]) + " " + str(normalizedStocks[bestB][0])
print "Best sharpe for " + bestStockA +" and " + bestStockB +" and " + bestStockC + " is " + str(bestSharpe)


end = time.clock()
print "All work took " + str(end - start) + " seconds."


pylab.plot(normalizedStocks[bestA])
pylab.legend(bestStockA)
pylab.plot(normalizedStocks[bestB])
pylab.legend(bestStockB)
pylab.plot(normalizedStocks[bestC])
pylab.legend(bestStockB)
pylab.plot((normalizedStocks[bestA]+normalizedStocks[bestB] + normalizedStocks[bestC]) / 3)
pylab.legend("Portfolio")
pylab.show()

