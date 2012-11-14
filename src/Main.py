# -*- coding: utf-8 -*-

import logging
from historical.StockListDownloader import StockListDownloader
from historical.yahoo.YahooAllDataDownloader import YahooAllDataDownloader

logging.basicConfig(level=logging.INFO)

#StockListDownloader("nasdaq").downloadAndConvertStockList()
#StockListDownloader("nyse").downloadAndConvertStockList()
#
YahooAllDataDownloader("nyse").downloadStocks()
# downloader.downloadStocks()
