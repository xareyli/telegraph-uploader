import time
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtCore import QObject, Signal
from API import Telegraph
import time
from store import store


class MainWindowService(QObject):
    progressChanged = Signal(bool, int, str)
    finished = Signal(str, int)

    def fileUploadedCallback(self, is_successful, number_uploaded, filepath):
        filename = filepath.split('\\')[-1]
        self.progressChanged.emit(is_successful, number_uploaded, filename)

    def upload(self):
        telegraph_api = Telegraph()

        start = time.time()
        article_url = telegraph_api.upload(store.dget('API', 'access_token'), store.dget('API', 'dir'), self.fileUploadedCallback)
        end = time.time()

        spent_time = int(end - start)

        self.finished.emit(article_url, spent_time)

    def chooseFolder(self):
        for x in range(75):
            self.progressChanged.emit(x)
            time.sleep(0.2)
        self.finished.emit()
