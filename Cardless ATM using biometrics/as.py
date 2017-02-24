import sys
from PyQt4 import QtCore, QtGui
from finalpinui import Ui_PinWindow

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ui =  Ui_PinWindow()
    ui.show()
    sys.exit(app.exec_())
