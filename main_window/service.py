import time
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtCore import QObject, Signal
from API import Telegraph
import time
from store import store


class MainWindowService(QObject):
    progressChanged = Signal(int)
    finished = Signal()

    def upload(self):
        telegraph_api = Telegraph()

        start = time.time()
        telegraph_api.upload(store.dget('API', 'access_token'), store.dget('API', 'dir'))
        end = time.time()

        print('Spent time: ' + str(end - start))

        self.progressChanged.emit('x')
        self.finished.emit()

    def chooseFolder(self):
        for x in range(75):
            self.progressChanged.emit(x)
            time.sleep(0.2)
        self.finished.emit()
