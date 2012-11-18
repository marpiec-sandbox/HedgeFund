from datetime import date
from historical.HistoricalDataRetrieval import HistoricalDataRetrieval
from statistics import statictics
from util.RemainingTimePrinter import RemainingTimePrinter
import numpy as np

class SharpeRatioOptimizer:

    _stocksProportions = [2/8, 4/8, 6/8, 7/8, 1, 8/7, 8/6, 8/4, 8/2]

    def findBestStocksWithHighestSharpeRatio(self, exchangeName, dateFrom, dateTo):
        stocksNormalizedCloseValues = self._loadNormalizedCloseValuesForStocks(exchangeName, dateFrom, dateTo)
        stockA, stockB, proportion, sharpeRatio = self._findBestSharpeRatioByBruteForce(stocksNormalizedCloseValues)
        return stockA[0], stockB[0], proportion, sharpeRatio

    def _loadNormalizedCloseValuesForStocks(self, exchangeName, dateFrom, dateTo):
        nasdaqDataRetrieval = HistoricalDataRetrieval(exchangeName)
        stockNames = nasdaqDataRetrieval.getListOfStocks()
        normalizedStocks = []

        timePrinter = RemainingTimePrinter("Loading " + exchangeName + " stocks data", len(stockNames))

        for a in range(len(stockNames)):
            timePrinter.printMessage(a)
            stockName = stockNames[a]
            stockArray = np.array(nasdaqDataRetrieval.loadAdjustedCloseValues(stockName, dateFrom, dateTo), np.float)
            if stockArray.shape[0] > 100 and stockArray[-1]/stockArray[0] > 1.2:
                normalizedStock = stockArray / stockArray[0]
                normalizedStocks.append((stockName, normalizedStock))

        timePrinter.printLastMessage()

        return normalizedStocks

    def _findBestSharpeRatioByBruteForce(self, stocksNormalizedCloseValues):
        stocksCount = len(stocksNormalizedCloseValues)
        timePrinter = RemainingTimePrinter("Searching for best sharpe ratio", stocksCount * stocksCount)
        bestStockA = None
        bestStockB = None
        bestProportion = None
        bestSharpe = -1000000
        for a in range(stocksCount):
            for b in range(stocksCount):
                for proportion in self._stocksProportions:
                    timePrinter.printMessage(b + a * stocksCount)
                    if a != b:
                        stockA = stocksNormalizedCloseValues[a]
                        stockB = stocksNormalizedCloseValues[b]
                        if stockA[1].shape[0] == stockB[1].shape[0]:
                            sharpeRatio = statictics.calculateSharpeRatioForStock(stockA[1] + stockB[1]*proportion)
                            if sharpeRatio > bestSharpe:
                                bestStockA = stockA
                                bestStockB = stockB
                                bestProportion = proportion
                                bestSharpe = sharpeRatio
        timePrinter.printLastMessage()
        return bestStockA, bestStockB, bestProportion, bestSharpe
