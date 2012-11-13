# -*- coding: utf-8 -*-

from YahooDataDownloader import *
import logging
from historical.StockListDownloader import StockListDownloader

logging.basicConfig(level=logging.INFO)


stockListDownloader = StockListDownloader()
stockListDownloader.downloadStockList()

downloader = HistoricalDataDownloader("nyse")
downloader.downloadStocks()
