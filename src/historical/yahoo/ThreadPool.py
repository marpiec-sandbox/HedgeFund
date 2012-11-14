from historical.yahoo.StockDownloaderWorker import StockDownloaderWorker

__author__ = 'marcin'


class ThreadPool:

    _threads = []

    def __init__(self, threadsCount):
        self._threadsCount = threadsCount

        for x in range(threadsCount):
            self._threads.append(StockDownloaderWorker())


    def getNextThread(self):