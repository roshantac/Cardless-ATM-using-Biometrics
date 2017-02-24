import sys
from PyQt4 import QtCore, QtGui
from Welcome import Ui_WelcomeWindow

class Main(QtGui.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()

        # build ui
        self.ui = Ui_WelcomeWindow()
        self.ui.setupUi(self)

     

  


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
