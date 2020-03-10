from PyQt5 import uic, QtWidgets, QtCore, QtGui
import window


class Browser(QtWidgets.QMainWindow, window.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.webEngineView.forward)
        self.pushButton_2.clicked.connect(self.webEngineView.back)
        self.pushButton_3.clicked.connect(self.run)
        self.pushButton_4.clicked.connect(self.webEngineView.reload)

        self.lineEdit.returnPressed.connect(self.pushButton_3.click)

    def run(self):
        self.webEngineView.load(QtCore.QUrl('https://' + self.lineEdit.text()))


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    browser = Browser()
    browser.setWindowTitle('Бряузер гугол родий')
    browser.show()
    sys.exit(app.exec_())
