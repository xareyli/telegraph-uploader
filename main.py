from main_window import MainWindow
from PySide import QtGui
import sys

# Create application
app = QtGui.QApplication(sys.argv)

main_window = MainWindow()
main_window.show()

app.exec_()
