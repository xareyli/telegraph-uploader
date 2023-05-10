import time
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtCore import QObject, Signal, Slot, QRunnable
from libs.telegraph import uploadImage, createPage
import time
from store import store
from utils import compressImagesDir
import os
import logging


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
        start = time.time()
        imgDir = store.dget('API', 'dir')

        if not os.path.exists('./temp'):
            os.makedirs('./temp')

        compressImagesDir(imgDir, './temp/')

        image_sources = self.uploadImagesFromDir('./temp/')

        article_url = False

        if len(image_sources):
            article_url = createPage(store.dget('API', 'access_token'), image_sources)

        end = time.time()

        spent_time = int(end - start)

        self.signals.finished.emit(article_url, spent_time)

    def uploadImagesFromDir(self, dir):
        image_sources = []
        number_uploaded = 1

        for path, dirs, files in os.walk(dir):
            for filename in files:
                if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')):
                    continue

                img_src, error = uploadImage(os.path.join(path, filename))

                if not error:
                    image_sources.append(img_src)
                else:
                    logging.warning('[API]: skipped "{}" due to "{}"'.format(filename, error))

                self.fileUploadedCallback(bool(img_src), number_uploaded, filename)

                number_uploaded += 1

        return image_sources
