from PySide import QtGui
from main_window.layout import Ui_Form
from main_window.service import MainWindowService
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtCore import QThreadPool
import logging
from event_bus import bus_instance, bus_messages
from utils import choose_archive, choose_folder
from store import store
import webbrowser


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
        self.ui.pushButton_3.clicked.connect(self.handleChooseSource)
        self.ui.pushButton.clicked.connect(self.handleClickedUpload)

    def handleLogin(self):
        bus_instance.publish(bus_messages.CreateTokenCommand())

    def handleChooseSource(self):
        """The 'select source' button click event listener

        Prompt user to choose a source directory or archive, and store the path in the appropriate configuration variable.
        Format and display the path to the user in the log.

        """
        # Determine whether to prompt for a directory or an archive.
        source_type = 'directory' if self.ui.verticalSlider.value() == 1 else 'archive'

        # Prompt the user for the source path.
        if source_type == 'directory':
            source_path = choose_folder()
        else:
            source_path = choose_archive()

        if source_path == None:
            return

        # Store the source path in the appropriate configuration variable.
        if source_type == 'directory':
            store.dset('API', 'archive', None)
            store.dset('API', 'dir', source_path)
        else:
            store.dset('API', 'dir', None)
            store.dset('API', 'archive', source_path)

        # Format the source path for display to the user.
        source_path = source_path.replace('\\', '/')
        source_parts = source_path.split('/')
        formatted_path = '/'.join(["{}\n".format(part) if i % 2 != 0 else "{}".format(part) for i, part in enumerate(source_parts)])

        # Log the chosen source path to the user.
        self.logToUser('APP', 'setting {}: \n'.format(source_type) + formatted_path)

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

    def handleUploadProgress(self, is_successful, number_uploaded, total_count, filename):
        self.ui.progressBar.setValue(number_uploaded / total_count * 100)

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
        upload_source = store.dget('API', 'dir') or store.dget('API', 'archive')

        if not store.dget('API', 'access_token'):
            self.logToUser('APP', 'Can\'t upload files because you didn\'t create account')
        elif not upload_source:
            self.logToUser('APP', 'Can\'t upload files because you didn\'t provide a directory with images')
        else:
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
