# -*- coding: utf-8 -*-
from Queue import Empty
import logging
from threading import Thread
import traceback

class ThreadWorker(Thread):
    def __init__(self, tasks, worker):
        Thread.__init__(self)
        self._tasks = tasks
        self._worker = worker
        pass

    def run(self):
        try:
            while True:
                task = self._tasks.get(False)
                tasksLeft = self._tasks.qsize()
                if tasksLeft % 100 == 0:
                    print str(tasksLeft) + " tasks left"

                try:
                    self._worker.work(task)
                except Exception:
                    traceback.print_exc()
                self._tasks.task_done()
        except Empty:
            pass





