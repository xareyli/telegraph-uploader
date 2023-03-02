from PySide import QtGui
from main_window.layout import Ui_Form
from main_window.service import MainWindowService
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtCore import QThread
import logging
from event_bus import bus_instance, bus_messages


class MainWindow():
    def __init__(self):
        logging.info('main window init')
        self.Form = QtGui.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        QCoreApplication.processEvents()

        # service
        self.service = MainWindowService()
        self.thread = QThread()
        self.service.moveToThread(self.thread)

    def show(self):
        logging.info('main window show')
        self.setHandlers()
        self.Form.show()

    def setHandlers(self):
        self.ui.pushButton_2.clicked.connect(self.handleLogin)
        self.ui.pushButton.clicked.connect(self.handleClickedUpload)

    def handleLogin(self):
        bus_instance.publish(bus_messages.CreateTokenCommand())

    def handleUploadProgress(self, x):
        self.ui.progressBar.setValue(x / 20 * 100)
        self.ui.textBrowser.setPlainText('[API]: couldn\'t load image_' + str(x) + '.png file, skipped due high size \n' + self.ui.textBrowser.toPlainText())

        if x == 20:
            self.ui.pushButton_2.setEnabled(True)

    def handleClickedUpload(self):
        self.service.progressChanged.connect(self.handleUploadProgress)
        self.thread.started.connect(self.service.upload)
        self.thread.start()
