from historical.yahoo.YahooOneStockDownloader import YahooOneStockDownloader

class StockDownloaderWorker:

    def __init__(self, exchangeName):
        self._exchangeName = exchangeName

    def work(self, stockName):
        YahooOneStockDownloader(self._exchangeName, stockName).downloadHistoricalPrizes()

