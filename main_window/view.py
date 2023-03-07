from PySide import QtGui
from main_window.layout import Ui_Form
from main_window.service import MainWindowService
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtCore import QThreadPool
from PySide.QtGui import QFileDialog, QMessageBox
import logging
from event_bus import bus_instance, bus_messages
from store import store
import webbrowser
import os


class MainWindow():
    def __init__(self):
        logging.info('main window init')
        self.Form = QtGui.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        QCoreApplication.processEvents()

        bus_instance.subscribe(bus_messages.TokenCreationDoneEvent(), self.onLoggedIn)
        bus_instance.subscribe(bus_messages.TokenCreationFailedEvent(), self.onLoginFailed)
        bus_instance.subscribe(bus_messages.SetSavedTokenEvent(), self.onSetSavedToken)

        self.threadpool = QThreadPool()

    def show(self):
        logging.info('main window show')
        self.setHandlers()
        self.Form.show()

    def setHandlers(self):
        self.ui.pushButton_2.clicked.connect(self.handleLogin)
        self.ui.pushButton_3.clicked.connect(self.handleChooseFolder)
        self.ui.pushButton.clicked.connect(self.handleClickedUpload)

    def handleLogin(self):
        bus_instance.publish(bus_messages.CreateTokenCommand())

    def handleChooseFolder(self):
        dir = None

        while not dir:
            dir = str(QFileDialog.getExistingDirectory(self.Form, "Select Directory"))
            if dir:
                store.dset('API', 'dir', dir)
            else:
                msgBox = QMessageBox()
                msgBox.setWindowTitle('Warning')
                msgBox.setText('You should select a folder')
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.exec()

        dir_splitted = dir.split('\\')
        dir_formated = ''

        for i in range(len(dir_splitted)):
            if i % 2 != 0:
                dir_formated = dir_formated + dir_splitted[i] + '\\\n'
            else:
                dir_formated = dir_formated + dir_splitted[i] + '\\'

        self.logToUser('APP', 'setting directory: \n' + dir_formated)

    def onLoggedIn(self, event):
        access_token = store.dget('API', 'access_token')
        self.logToUser('API', 'Token generated: \n' + access_token)

        self.unblockUi()

    def onLoginFailed(self, event):
        self.logToUser('API', 'Authorization failed, please try again. If the error persists, contact your developer tg: @xareyli')

        self.unblockUi()

    def onSetSavedToken(self, event):
        self.logToUser('APP', 'Token is loaded from file')

    def blockUi(self):
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton_3.setEnabled(False)

    def unblockUi(self):
        self.ui.pushButton.setEnabled(True)
        self.ui.pushButton_2.setEnabled(True)
        self.ui.pushButton_3.setEnabled(True)

    def handleUploadProgress(self, is_successful, number_uploaded, filename):
        self.ui.progressBar.setValue(number_uploaded / self.filesCount * 100)

        if not is_successful:
            self.logToUser('API', 'couldn\'t load ' + filename + ' file')

    def handleUploadDone(self, article_url, spent_time):
        if article_url:
            self.logToUser('API', 'done in {} seconds'.format(str(spent_time)))
            webbrowser.open(article_url)
        else:
            self.logToUser('API', 'unable to upload ¯\_(ツ)_/¯')

        self.unblockUi()

    def handleClickedUpload(self):
        if not store.dget('API', 'access_token'):
            self.logToUser('APP', 'Can\'t upload files because you didn\'t create account')
        elif not store.dget('API', 'dir'):
            self.logToUser('APP', 'Can\'t upload files because you didn\'t provide a directory with images')
        else:
            self.filesCount = len([name for name in os.listdir(store.dget('API', 'dir'))])

            service = MainWindowService()

            service.signals.progressChanged.connect(self.handleUploadProgress)
            service.signals.finished.connect(self.handleUploadDone)

            self.threadpool.start(service)

            self.blockUi()
            self.ui.progressBar.setValue(0)
            self.logToUser('API', 'starting upload')

    def logToUser(self, where_occured, message):
        resulting_message = '[{}]: {}'.format(where_occured, message)

        resulting_message = resulting_message + '\n-----------------------------------\n' + self.ui.textBrowser.toPlainText()

        self.ui.textBrowser.setPlainText(resulting_message)
