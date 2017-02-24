# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Acctyp.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Selectoption(object):
    def setupUi(self, Selectoption):
        Selectoption.setObjectName(_fromUtf8("Selectoption"))
        Selectoption.resize(800, 600)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(198, 19, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(198, 19, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(198, 19, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(198, 19, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        Selectoption.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("TeX Gyre Termes Math"))
        Selectoption.setFont(font)
        self.centralwidget = QtGui.QWidget(Selectoption)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 10, 661, 51))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 120, 421, 41))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(630, 190, 81, 51))
        self.pushButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../image/rarorw.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(80, 80))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 290, 81, 51))
        self.pushButton_2.setText(_fromUtf8(""))
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(400, 200, 201, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(400, 300, 191, 41))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        Selectoption.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Selectoption)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Selectoption.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Selectoption)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Selectoption.setStatusBar(self.statusbar)

        self.retranslateUi(Selectoption)
        QtCore.QMetaObject.connectSlotsByName(Selectoption)

    def retranslateUi(self, Selectoption):
        Selectoption.setWindowTitle(_translate("Selectoption", "Optionwindow", None))
        self.label.setText(_translate("Selectoption", "<html><head/><body><p><span style=\" font-size:22pt; font-style:italic; color:#ffffff;\">Hii </span></p></body></html>", None))
        self.label_2.setText(_translate("Selectoption", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">Select Account Type:</span></p></body></html>", None))
        self.label_3.setText(_translate("Selectoption", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; color:#ffffff;\">Current Account</span></p></body></html>", None))
        self.label_4.setText(_translate("Selectoption", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; color:#ffffff;\">Saving Account</span></p></body></html>", None))

