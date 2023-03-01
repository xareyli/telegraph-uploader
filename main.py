from PySide import QtCore, QtGui
from main_window import Ui_Form
import sys
import time
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtCore import QObject, Signal, QThread


# Create application
app = QtGui.QApplication(sys.argv)

# Hooks
class LongPythonThread(QObject):    
    thread_finished = Signal(str)

    def __init__(self):
        super(LongPythonThread,self).__init__()

    def long_thread(self):
        for x in range(0, 100):
            message = '[API]: couldn\'t load image_' + str(x) + '.png file, skipped due high size \n'
            ui.textBrowser.setPlainText(ui.textBrowser.toPlainText() + message)
            ui.progressBar.setProperty("value", x)
            time.sleep(1)
        self.thread_finished.emit()


class Worker(QObject):
    progressChanged = Signal(int)

    def upload(self):
        for x in range(1, 21):
            time.sleep(0.6)
            self.progressChanged.emit(x)
        print(x)
        print('thread is done')


# Create form and init UI
Form = QtGui.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
QCoreApplication.processEvents()
Form.show()

def processWork(x):
    ui.progressBar.setValue(x / 20 * 100)
    ui.textBrowser.setPlainText('[API]: couldn\'t load image_' + str(x) + '.png file, skipped due high size \n' + ui.textBrowser.toPlainText())

    if x == 20:
        ui.pushButton_2.setEnabled(True)


worker = Worker()
thread = QThread()
# ui.progressBar
worker.moveToThread(thread)
worker.progressChanged.connect(processWork)
thread.started.connect(worker.upload)

def start():
    print('thread started')
    thread.start()
    ui.pushButton_2.setEnabled(False)

ui.pushButton_2.clicked.connect(start)

app.exec_()
