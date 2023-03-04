from PySide import QtGui
from auth.layout import Ui_Form
from PySide.QtCore import *
from PySide.QtGui import *
import logging
from auth.service import AuthWindowService
import webbrowser
from event_bus import bus_instance, bus_messages


class AuthWindow:
    def __init__(self):
        logging.info('auth window init')
        self.Form = QtGui.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        QCoreApplication.processEvents()

        # service
        self.service = AuthWindowService()

    def setHandlers(self):
        self.ui.pushButton.clicked.connect(self.handleSubmit)

    def unsetHandlers(self):
        self.ui.pushButton.clicked.disconnect(self.handleSubmit)

    def handleSubmit(self):
        short_name = self.ui.lineEdit.text()
        author_name = self.ui.lineEdit_2.text()

        auth_url = self.service.registerUser(short_name, author_name)

        webbrowser.open(auth_url)

        bus_instance.publish(bus_messages.TokenCreationDoneEvent())
        self.hide()

    def show(self):
        logging.info('auth window show')
        self.setHandlers()
        self.Form.show()

    def hide(self):
        logging.info('auth window hide')
        self.unsetHandlers()
        self.Form.hide()
