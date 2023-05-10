from PySide.QtGui import QMessageBox, QFileDialog
import os


VALID_ARCHIVE_EXTENSIONS = ('.zip', '.rar', '.7z')

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


def choose_folder():
    """Asks the user for directory

    Prompts the user to select a directory and returns the directory path if a valid directory is selected.
    Returns None if the user cancels the dialog or selects an invalid directory.

    """
    try:
        directory = str(QFileDialog.getExistingDirectory(None, "Select Directory"))

        if directory and os.path.isdir(directory):
            return directory
        else:
            show_message_box('warning', 'You should select a folder')
            return None
    except Exception as e:
        show_message_box('error', 'Error: {}'.format(e))
        return None


def choose_archive():
    """Asks the user for archive

    Prompts the user to select an archive file containing images, and returns the path to the selected file.

    """
    try:
        archive = str(QFileDialog.getOpenFileName(None, "Select archive with images", '*', "Archives (*.zip *.rar *.7z)")[0])

        if os.path.splitext(archive)[1] in VALID_ARCHIVE_EXTENSIONS:
            return archive
        else:
            show_message_box('warning', 'You should select an archive')
            return None
    except Exception as e:
        show_message_box('error', 'Error: {}'.format(e))
        return None
