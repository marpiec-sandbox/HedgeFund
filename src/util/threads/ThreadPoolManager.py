# -*- coding: utf-8 -*-
from Queue import Queue
from util.threads.ThreadWorker import ThreadWorker

class ThreadPoolManager:
    def __init__(self, threadCount):
        self._tasksQueue = Queue()
        self._threadCount = threadCount

    def addTasks(self, tasks):
        for task in tasks:
            self._tasksQueue.put(task)

    def startWork(self, worker):
        for _ in range(self._threadCount):
            ThreadWorker(self._tasksQueue, worker).start()
        self._tasksQueue.join()