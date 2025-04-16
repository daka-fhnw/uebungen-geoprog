import os
import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *


class Fenster(QMainWindow):

    def __init__(self):
        super().__init__()
        self.load_ui()
        self.prepare_ui()
        self.show()

    def load_ui(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        loadUi(f'{dir_path}/showmap.ui', self)

    def prepare_ui(self):
        self.button.clicked.connect(self.show_on_map)

    def show_on_map(self):
        lon = self.edit_laenge.text()
        lat = self.edit_breite.text()
        if lon != '' and lat != '':
            link = f'https://www.google.ch/maps/place/{lat},{lon}'
            QDesktopServices.openUrl(QUrl(link))


def main():
    app = QApplication(sys.argv)
    mainwindow = Fenster()
    mainwindow.raise_()
    app.exec_()


if __name__ == '__main__':
    main()
