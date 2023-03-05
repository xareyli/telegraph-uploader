import config
from PySide import QtGui
import sys

# Create application before importing windows
app = QtGui.QApplication(sys.argv)

from main_window import main_window
import auth
import start_hooks

main_window.show()

app.exec_()
