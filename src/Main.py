# -*- coding: utf-8 -*-

from YahooDataDownloader import *
import logging
from historical.StockListDownloader import StockListDownloader

logging.basicConfig(level=logging.INFO)

StockListDownloader("nasdaq").downloadAndConvertStockList()
StockListDownloader("nyse").downloadAndConvertStockList()

# downloader = HistoricalDataDownloader("nyse")
# downloader.downloadStocks()
