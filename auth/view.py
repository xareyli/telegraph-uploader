from PySide import QtGui
from auth.layout import Ui_Form
from PySide.QtCore import *
from PySide.QtGui import *
import logging
from auth.service import AuthWindowService
import webbrowser
from event_bus import bus_instance, bus_messages
from utils import show_message_box


class AuthWidget(QtGui.QWidget):
    def __init__(self, closeHandler):
        super().__init__()

        self.closeHandler = closeHandler

    def closeEvent(self, event):
        self.closeHandler()


class AuthWindow:
    def __init__(self):
        logging.info('auth window init')
        self.Form = AuthWidget(self.unsetHandlers)
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        QCoreApplication.processEvents()

        # service
        self.service = AuthWindowService()

    def setHandlers(self):
        self.ui.pushButton.clicked.connect(self.handleSubmit)

    def unsetHandlers(self):
        print('unsetting handlers')
        self.ui.pushButton.clicked.disconnect(self.handleSubmit)

    def handleSubmit(self):
        short_name = self.ui.lineEdit.text()
        author_name = self.ui.lineEdit_2.text()

        if not short_name.strip():
            show_message_box('warning', 'short name is empty')
            return

        if not author_name.strip():
            show_message_box('warning', 'author name is empty')
            return

        auth_url = self.service.registerUser(short_name, author_name)

        if not auth_url:
            bus_instance.publish(bus_messages.TokenCreationFailedEvent())
            self.hide()
            return

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
