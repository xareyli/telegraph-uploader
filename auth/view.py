from PySide import QtGui
from auth.layout import Ui_Form
from PySide.QtCore import *
from PySide.QtGui import *
import logging


class AuthWindow:
    def __init__(self):
        logging.info('auth window init')
        self.Form = QtGui.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        QCoreApplication.processEvents()

    def setHandlers(self):
        pass

    def show(self):
        logging.info('auth window show')
        self.setHandlers()
        self.Form.show()
