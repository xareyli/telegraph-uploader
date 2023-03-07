# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\web\pyproject\qtTelegraphUploader\auth-window.ui'
#
# Created: Wed Mar  1 22:17:47 2023
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(402, 290)
        Form.setStyleSheet("background-color: #F2E9E4;")
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 30, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Red Hat Mono")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(70, 60, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Red Hat Mono")
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: #FFF;\n"
"border-radius: 2px;\n"
"border: 1px solid #9A8C98;\n"
"padding: 0 5px;")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(150, 120, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Red Hat Mono")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 150, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Red Hat Mono")
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: #FFF;\n"
"border-radius: 2px;\n"
"border: 1px solid #9A8C98;\n"
"padding: 0 5px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 210, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Red Hat Mono")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton.setStyleSheet(".QPushButton {\n"
"    background-color: #4A4E69;\n"
"    color: #FFFCFB;\n"
"    border-radius: 11px;\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"    background-color: rgba(74,78,105, 70%);\n"
"}\n"
".QPushButton:focus {\n"
"    outline: 0;\n"
"}")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Account name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Short name", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Confirm", None, QtGui.QApplication.UnicodeUTF8))
