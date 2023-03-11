import config
from PySide import QtGui
import sys
import os

import ctypes
myappid = 'xareyli.telegraph-uploader.app.01' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


# Create application before importing windows
app = QtGui.QApplication(sys.argv)

app.setWindowIcon(QtGui.QIcon(os.path.join('assets', 'icon.png')))

from main_window import main_window
import auth
import start_hooks

main_window.show()

start_hooks.on_app_started()

app.exec_()
