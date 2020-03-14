import os

from PyQt5 import QtWidgets, QtCore

import window


class Browser(QtWidgets.QMainWindow, window.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.webEngineView.forward)
        self.pushButton_2.clicked.connect(self.webEngineView.back)
        self.pushButton_3.clicked.connect(self.browse)
        self.pushButton_4.clicked.connect(self.webEngineView.reload)
        self.pushButton_5.clicked.connect(self.save)

        self.lineEdit.returnPressed.connect(self.pushButton_3.click)

        self.webEngineView.urlChanged.connect(self.changeUrl)
        self.webEngineView.loadProgress.connect(self.showProgress)

    def browse(self):
        url = self.lineEdit.text()
        if url.startswith('http://') or url.startswith('https://'):
            self.webEngineView.load(QtCore.QUrl(url))
        else:
            self.webEngineView.load(QtCore.QUrl('http://' + self.lineEdit.text()))

    def changeUrl(self):
        self.lineEdit.setText(self.webEngineView.url().url())

    def showProgress(self, progress):
        self.statusbar.showMessage(f'Прогресс загрузки страницы: {progress}%', msecs=3000)

    def save(self):
        dialog = QtWidgets.QFileDialog.getSaveFileName(parent=self,
                                                       caption='Сохранение HTML-страницы',
                                                       directory=QtCore.QDir.homePath(),
                                                       filter='All (*)')
        if dialog[0]:
            path_to_save, filename = os.path.split(dialog[0])
            self.webEngineView.page().save(os.path.join(path_to_save, filename), format=0)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    browser = Browser()
    browser.setWindowTitle('Бряузер гугол родий')
    browser.show()
    sys.exit(app.exec_())
