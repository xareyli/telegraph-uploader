import time
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtCore import QObject, Signal, Slot, QRunnable
from API import Telegraph
import time
from store import store


class _Signals(QObject):
    progressChanged = Signal(bool, int, str)
    finished = Signal(str, int)


class MainWindowService(QRunnable):
    def __init__(self) -> None:
        super().__init__()
        self.signals = _Signals()

    def fileUploadedCallback(self, is_successful, number_uploaded, filepath):
        filename = filepath.split('\\')[-1]
        self.signals.progressChanged.emit(is_successful, number_uploaded, filename)

    @Slot()
    def run(self):
        telegraph_api = Telegraph()

        start = time.time()
        article_url = telegraph_api.upload(store.dget('API', 'access_token'), store.dget('API', 'dir'), self.fileUploadedCallback)
        end = time.time()

        spent_time = int(end - start)

        self.signals.finished.emit(article_url, spent_time)
