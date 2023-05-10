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
from zipfile import ZipFile
import shutil


class _Signals(QObject):
    progressChanged = Signal(bool, int, int, str)
    finished = Signal(str, int)


class MainWindowService(QRunnable):
    def __init__(self) -> None:
        super().__init__()
        self.signals = _Signals()

    def fileUploadedCallback(self, is_successful, number_uploaded, total_count, filepath):
        filename = filepath.split('\\')[-1]
        self.signals.progressChanged.emit(is_successful, number_uploaded, total_count, filename)

    @Slot()
    def run(self):
        start = time.time()

        if not os.path.exists('./temp'):
            os.makedirs('./temp')

        img_dir = store.dget('API', 'dir') or store.dget('API', 'archive')

        if os.path.isfile(img_dir):
            with ZipFile(img_dir, 'r') as zObject:
                zObject.extractall(path='./temp_archive')
                img_dir = './temp_archive'

        compressImagesDir(img_dir, './temp/')

        image_sources = self.uploadImagesFromDir('./temp/')

        article_url = False

        if len(image_sources):
            article_url = createPage(store.dget('API', 'access_token'), image_sources)

        shutil.rmtree('./temp')
        shutil.rmtree('./temp_archive')

        end = time.time()

        spent_time = int(end - start)

        self.signals.finished.emit(article_url, spent_time)

    def uploadImagesFromDir(self, dir):
        image_sources = []
        number_uploaded = 1
        total_count = 0

        for path, _, files in os.walk(dir):
            for filename in files:
                if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')):
                    total_count += 1

            for filename in files:
                if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')):
                    continue

                img_src, error = uploadImage(os.path.join(path, filename))

                if not error:
                    image_sources.append(img_src)
                else:
                    logging.warning('[API]: skipped "{}" due to "{}"'.format(filename, error))

                self.fileUploadedCallback(bool(img_src), number_uploaded, total_count, filename)

                number_uploaded += 1

        return image_sources
