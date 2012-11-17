# -*- coding: utf-8 -*-

import numpy as np

def calculateSharpeRatioForStock(stocks):
    dailyReturn = stocks[1:] / stocks[:-1] - 1
    standardDeviation = np.std(dailyReturn)
    average = np.average(dailyReturn)
    K = np.sqrt(250)
    return K * average / standardDeviation


def calculateCorrelationOfStocks(stockA, stockB):
    dailyReturnA = stockA[1:] / stockA[:-1] - 1
    dailyReturnB = stockB[1:] / stockB[:-1] - 1
    return np.std(dailyReturnA, dailyReturnB)