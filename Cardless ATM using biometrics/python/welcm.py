import sys
from PyQt4 import QtCore, QtGui
from Welcome import Ui_WelcomeWindow

class Main(QtGui.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()

        # build ui
        self.ui1 = Ui_WelcomeWindow()
        self.ui1.show()
	
  

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    main.hide()	
    sys.exit(app.exec_())
