# -*- coding: utf-8 -*-

from HistoricalDataDownloader import *
import logging

logging.basicConfig(level=logging.INFO)

downloader = HistoricalDataDownloader("nyse")
downloader.downloadStocks()
