# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Welcome.ui'
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

class Ui_WelcomeWindow(object):
    def setupUi(self, WelcomeWindow):
        WelcomeWindow.setObjectName(_fromUtf8("WelcomeWindow"))
        WelcomeWindow.resize(881, 583)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(198, 14, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(198, 14, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(198, 14, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(198, 14, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        WelcomeWindow.setPalette(palette)
        self.centralwidget = QtGui.QWidget(WelcomeWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 30, 381, 201))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Utopia"))
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 330, 111, 151))
        self.pushButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../image/pr2.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(150, 150))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 250, 691, 81))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        WelcomeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(WelcomeWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 881, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        WelcomeWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(WelcomeWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        WelcomeWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(WelcomeWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        WelcomeWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(WelcomeWindow)
        QtCore.QMetaObject.connectSlotsByName(WelcomeWindow)

    def retranslateUi(self, WelcomeWindow):
        WelcomeWindow.setWindowTitle(_translate("WelcomeWindow", "WelcomeWindow", None))
        self.label.setText(_translate("WelcomeWindow", "<html><head/><body><p><span style=\" font-size:72pt; color:#ffffff;\">Hello.</span></p></body></html>", None))
        self.label_2.setText(_translate("WelcomeWindow", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; color:#ffffff;\">Please place your finger on the sensor to continue</span></p></body></html>", None))
        self.toolBar.setWindowTitle(_translate("WelcomeWindow", "toolBar", None))

