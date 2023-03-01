import time
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtCore import QObject, Signal


class MainWindowService(QObject):
    progressChanged = Signal(int)
    finished = Signal()

    def upload(self):
        for x in range(1, 21):
            time.sleep(0.2)
            self.progressChanged.emit(x)
        self.finished.emit()

    def chooseFolder(self):
        for x in range(75):
            self.progressChanged.emit(x)
            time.sleep(0.2)
        self.finished.emit()
