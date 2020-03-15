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
        self.pushButton_6.clicked.connect(self.show_history)

        self.lineEdit.returnPressed.connect(self.pushButton_3.click)

        self.webEngineView.urlChanged.connect(self.change_url)
        self.webEngineView.loadProgress.connect(self.show_progress)

        self.tableWidget.setHidden(True)

    def browse(self):
        url = self.lineEdit.text()
        if url.startswith('http://') or url.startswith('https://'):
            self.webEngineView.load(QtCore.QUrl(url))
        else:
            self.webEngineView.load(QtCore.QUrl('http://' + self.lineEdit.text()))

    def show_history(self):
        if self.tableWidget.isHidden():
            self.tableWidget.setVisible(True)

            history = list(map(lambda item:
                               {
                                   'title': QtWidgets.QTableWidgetItem(item.title()),
                                   'url': QtWidgets.QTableWidgetItem(item.url().url())
                               },
                               self.webEngineView.history().items()))[::-1]
            count = len(history)
            self.tableWidget.setRowCount(count)
            for i in range(count):
                self.tableWidget.setItem(i, 0, history[i]['title'])
                self.tableWidget.setItem(i, 1, history[i]['url'])
        else:
            self.tableWidget.setHidden(True)
            self.tableWidget.clearContents()

    def change_url(self):
        self.lineEdit.setText(self.webEngineView.url().url())

    def show_progress(self, progress):
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
    browser.showMaximized()
    sys.exit(app.exec_())
