# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Enteramnt.ui'
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

class Ui_PinWindow(object):
    def setupUi(self, PinWindow):
        PinWindow.setObjectName(_fromUtf8("PinWindow"))
        PinWindow.setEnabled(True)
        PinWindow.resize(790, 619)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(198, 19, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(198, 19, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 158, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(198, 19, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(198, 19, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        PinWindow.setPalette(palette)
        PinWindow.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        PinWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        PinWindow.setAutoFillBackground(True)
        PinWindow.setIconSize(QtCore.QSize(35, 35))
        PinWindow.setDocumentMode(False)
        self.centralwidget = QtGui.QWidget(PinWindow)
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.push1 = QtGui.QPushButton(self.centralwidget)
        self.push1.setGeometry(QtCore.QRect(202, 240, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.push1.setFont(font)
        self.push1.setObjectName(_fromUtf8("push1"))
        self.push2 = QtGui.QPushButton(self.centralwidget)
        self.push2.setGeometry(QtCore.QRect(320, 240, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.push2.setFont(font)
        self.push2.setObjectName(_fromUtf8("push2"))
        self.push3 = QtGui.QPushButton(self.centralwidget)
        self.push3.setGeometry(QtCore.QRect(430, 240, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.push3.setFont(font)
        self.push3.setObjectName(_fromUtf8("push3"))
        self.push4 = QtGui.QPushButton(self.centralwidget)
        self.push4.setGeometry(QtCore.QRect(202, 310, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.push4.setFont(font)
        self.push4.setObjectName(_fromUtf8("push4"))
        self.push5 = QtGui.QPushButton(self.centralwidget)
        self.push5.setGeometry(QtCore.QRect(320, 310, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.push5.setFont(font)
        self.push5.setObjectName(_fromUtf8("push5"))
        self.push6 = QtGui.QPushButton(self.centralwidget)
        self.push6.setGeometry(QtCore.QRect(430, 310, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.push6.setFont(font)
        self.push6.setObjectName(_fromUtf8("push6"))
        self.push7 = QtGui.QPushButton(self.centralwidget)
        self.push7.setGeometry(QtCore.QRect(200, 380, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.push7.setFont(font)
        self.push7.setObjectName(_fromUtf8("push7"))
        self.push8 = QtGui.QPushButton(self.centralwidget)
        self.push8.setGeometry(QtCore.QRect(320, 380, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.push8.setFont(font)
        self.push8.setObjectName(_fromUtf8("push8"))
        self.push9 = QtGui.QPushButton(self.centralwidget)
        self.push9.setGeometry(QtCore.QRect(430, 380, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.push9.setFont(font)
        self.push9.setObjectName(_fromUtf8("push9"))
        self.push0 = QtGui.QPushButton(self.centralwidget)
        self.push0.setGeometry(QtCore.QRect(320, 450, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.push0.setFont(font)
        self.push0.setObjectName(_fromUtf8("push0"))
        self.pushclear = QtGui.QPushButton(self.centralwidget)
        self.pushclear.setGeometry(QtCore.QRect(540, 270, 111, 81))
        self.pushclear.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../image/larow.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushclear.setIcon(icon)
        self.pushclear.setIconSize(QtCore.QSize(150, 90))
        self.pushclear.setObjectName(_fromUtf8("pushclear"))
        self.pushcancel = QtGui.QPushButton(self.centralwidget)
        self.pushcancel.setGeometry(QtCore.QRect(540, 370, 111, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(90, 90, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(111, 111, 111))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(163, 163, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 90, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(111, 111, 111))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(163, 163, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 90, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(111, 111, 111))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.pushcancel.setPalette(palette)
        self.pushcancel.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../image/cancl.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushcancel.setIcon(icon1)
        self.pushcancel.setIconSize(QtCore.QSize(150, 80))
        self.pushcancel.setObjectName(_fromUtf8("pushcancel"))
        self.pushaccs = QtGui.QPushButton(self.centralwidget)
        self.pushaccs.setGeometry(QtCore.QRect(540, 160, 111, 81))
        self.pushaccs.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../image/rarorw.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushaccs.setIcon(icon2)
        self.pushaccs.setIconSize(QtCore.QSize(150, 90))
        self.pushaccs.setObjectName(_fromUtf8("pushaccs"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 40, 581, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 158, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 158, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Link, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Latin Modern Roman Demi"))
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(200, 170, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(660, 180, 68, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("TeX Gyre Termes Math"))
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(660, 290, 81, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("TeX Gyre Termes Math"))
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(660, 380, 121, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tibetan Machine Uni"))
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 10, 511, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("TeX Gyre Termes Math"))
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        PinWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(PinWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 790, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        PinWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(PinWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        PinWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PinWindow)
        QtCore.QMetaObject.connectSlotsByName(PinWindow)

    def retranslateUi(self, PinWindow):
        PinWindow.setWindowTitle(_translate("PinWindow", "PinWindow", None))
        self.push1.setText(_translate("PinWindow", "1", None))
        self.push2.setText(_translate("PinWindow", "2", None))
        self.push3.setText(_translate("PinWindow", "3", None))
        self.push4.setText(_translate("PinWindow", "4", None))
        self.push5.setText(_translate("PinWindow", "5", None))
        self.push6.setText(_translate("PinWindow", "6", None))
        self.push7.setText(_translate("PinWindow", "7", None))
        self.push8.setText(_translate("PinWindow", "8", None))
        self.push9.setText(_translate("PinWindow", "9", None))
        self.push0.setText(_translate("PinWindow", "0", None))
        self.label.setText(_translate("PinWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">Enter Amount in multiples of hundreds</span></p></body></html>", None))
        self.label_2.setText(_translate("PinWindow", "<html><head/><body><p><span style=\" font-size:22pt;\">GO</span></p></body></html>", None))
        self.label_3.setText(_translate("PinWindow", "<html><head/><body><p><span style=\" font-size:22pt;\">BACK</span></p></body></html>", None))
        self.label_4.setText(_translate("PinWindow", "<html><head/><body><p><span style=\" font-size:20pt; color:#0b0b0b;\">CANCEL</span></p></body></html>", None))
        self.label_5.setText(_translate("PinWindow", "<html><head/><body><p><span style=\" font-size:22pt; font-style:italic; color:#ffffff;\">Hii</span></p></body></html>", None))

