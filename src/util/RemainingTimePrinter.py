import time
from util import StringUtil

class RemainingTimePrinter:

    def __init__(self, message, allTasksCount):
        self._start = time.clock()
        self._allTasksCount = allTasksCount
        self._lastTimePrinted = time.clock() - 2
        self._message = message

    def printMessage(self, tasksDone):
        percentDone = float(tasksDone)/float(self._allTasksCount)*100.0
        now = time.clock()

        if now - self._lastTimePrinted > 1:
            if tasksDone > 0:
                timeRemaining = (now - self._start) / \
                            (float(tasksDone)/float(self._allTasksCount)) * \
                            (float(self._allTasksCount - tasksDone)/float(self._allTasksCount))
            else:
                timeRemaining = -1
            self._lastTimePrinted = now
            print self._message + ".... " + ("%.1f" % percentDone) + "% done, time ramaining",
            if timeRemaining < 0:
                print "unknown"
            else:
                print StringUtil.formatDuration(timeRemaining)

    def printLastMessage(self):
        now = time.clock()
        print "Work done in " + StringUtil.formatDuration(now - self._start) + " seconds"

