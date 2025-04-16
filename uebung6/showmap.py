import os
import sys
import urllib.parse

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
        laenge = urllib.parse.quote(self.edit_laenge.text())
        breite = urllib.parse.quote(self.edit_breite.text())
        if laenge != '' and breite != '':
            link = f'https://www.google.ch/maps/place/{breite},{laenge}'
            QDesktopServices.openUrl(QUrl(link))


def main():
    app = QApplication(sys.argv)
    mainwindow = Fenster()
    mainwindow.raise_()
    app.exec_()


if __name__ == '__main__':
    main()
