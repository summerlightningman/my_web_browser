from PyQt5 import QtWidgets
from window import Ui_MainWindow

class Browser(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    browser = Browser()
    browser.setWindowTitle('Бряузер гугол родий')
    browser.show()
    sys.exit(app.exec_())
