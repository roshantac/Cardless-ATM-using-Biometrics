import sys
from PyQt4 import QtCore, QtGui
from finalpinui import Ui_PinWindow

class Main(QtGui.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()

        # build ui
        self.ui = Ui_PinWindow()
        self.ui.setupUi(self)

     

  


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
