# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\web\pyproject\qtTelegraphUploader\main-window.ui'
#
# Created: Mon Feb 27 22:05:08 2023
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.setFixedSize(720, 552)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color: #F2E9E4;\n"
"")
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 0, 181, 551))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Red Hat Mono")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton_2.setStyleSheet(".QPushButton {\n"
"    width: 177px;\n"
"    height: 101px;\n"
"    border-radius: 15px;\n"
"    background-color: #22223B;\n"
"    color: #F2E9E4;\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"    background-color: rgba(34,34,59, 70%);\n"
"}\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Red Hat Mono")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton_3.setAccessibleName("")
        self.pushButton_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_3.setStyleSheet(".QPushButton {\n"
"    background-color: #9A8C98;\n"
"    border-radius: 15px;\n"
"    color: #F2E9E4;\n"
"    height: 101px;\n"
"    width: 177px;\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"    background-color: rgba(154,140,152, 70%);\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Red Hat Mono")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton.setStyleSheet(".QPushButton {\n"
"    width: 177px;\n"
"    height: 101px;\n"
"    border-radius: 15px;\n"
"    background-color: #C9ADA7;\n"
"    color: #FDF8F5;\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"    background-color: rgba(201,173,167, 70%);\n"
"}\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(290, 137, 371, 351))
        font = QtGui.QFont()
        font.setFamily("Red Hat Mono")
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("QTextBrowser {\n"
"    background: white;\n"
"    border: 1px solid #9A8C98;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background:white;\n"
"    width:6px;    \n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"  border-radius: 50%;\n"
"    background: #22223B;\n"
"    min-height: 0px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    background: red;\n"
"    height: 0 px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"")
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(440, 60, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Red Hat Mono")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.progressBar = QtGui.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(290, 90, 371, 31))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    background: white;\n"
"    border-style: outset;\n"
"    border: 1px solid #9A8C98;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #C2FF74;\n"
"     border-right: 1px solid #9A8C98;\n"
"}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle('Telegraph uploader')
        self.pushButton_2.setText(QtGui.QApplication.translate("Form", "Create\n"
"Token", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Form", "Choose\n"
"Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Upload", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Red Hat Mono\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Progress", None, QtGui.QApplication.UnicodeUTF8))
