from PySide.QtGui import QMessageBox

messageBoxTypes = {
    'warning': {
        'title': 'Warning',
        'icon': QMessageBox.Warning
    }
}

def show_message_box(level, message):
    mb_type = messageBoxTypes[level]

    msgBox = QMessageBox()
    msgBox.setWindowTitle(mb_type['title'])
    msgBox.setText(message)
    msgBox.setIcon(mb_type['icon'])
    msgBox.exec()
