import time
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtCore import QObject, Signal, Slot, QRunnable
from libs.telegraph import uploadImage, createPage
import time
from store import store
from libs.image import compressImage
import os
import logging
from zipfile import ZipFile
import shutil
import threading


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

        self.compressImagesDir(img_dir, './temp/')

        image_sources = self.uploadImagesFromDir('./temp/')

        article_url = False

        if len(image_sources):
            article_url = createPage(store.dget('API', 'access_token'), image_sources)

        if os.path.exists('./temp'):
            shutil.rmtree('./temp')

        if os.path.exists('./temp_archive'):
            shutil.rmtree('./temp_archive')

        end = time.time()

        spent_time = int(end - start)

        self.signals.finished.emit(article_url, spent_time)

    def uploadImagesFromDir(self, dir):
        image_sources = []
        number_uploaded = 1

        for path, _, files in os.walk(dir):
            for filename in files:
                try:
                    img_src = uploadImage(os.path.join(path, filename))

                    image_sources.append(img_src)

                    self.fileUploadedCallback(bool(img_src), number_uploaded, len(files), filename)

                    number_uploaded += 1
                except Exception as e:
                    logging.warning('[API]: skipped "{}" due to "{}"'.format(filename, str(e)))

        return image_sources

    def compressImagesDir(self, img_dir, save_dir):
        def compressImagesArray(path, files, save_dir):
            for filename in files:
                if filename.lower().split('.')[-1] in ('jpg', 'jpeg', 'png'):
                    fullpath = os.path.join(path, filename)

                    compressImage(fullpath, save_dir, (5500, 3500), 5)


        for path, _, files in os.walk(img_dir):
            l = len(files) // 3

            ftFiles = files[:l] # first thread files
            stFiles = files[l:l * 2] # second thread files
            ttFiles = files[l * 2:] # third thread files

            ft = threading.Thread(target=compressImagesArray, args=(path, ftFiles, save_dir))
            ft.start()

            st = threading.Thread(target=compressImagesArray, args=(path, stFiles, save_dir))
            st.start()

            tt = threading.Thread(target=compressImagesArray, args=(path, ttFiles, save_dir))
            tt.start()

            ft.join()
            st.join()
            tt.join()
