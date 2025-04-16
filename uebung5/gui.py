import sys

import csv
import urllib.parse
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Fenster(QMainWindow):

    def __init__(self):
        super().__init__()
        self.create_menubar()
        self.create_layout()

    def create_menubar(self):
        menubar = self.menuBar()

        load_action = QAction("Laden", self)
        load_action.triggered.connect(self.load)

        save_action = QAction("Speichern", self)
        save_action.triggered.connect(self.save)

        quit_action = QAction("Beenden", self)
        quit_action.triggered.connect(self.quit)

        file_menu = menubar.addMenu("Datei")
        file_menu.addAction(load_action)
        file_menu.addAction(save_action)
        file_menu.addAction(quit_action)

        show_on_map_action = QAction("Auf Karte zeigen", self)
        show_on_map_action.triggered.connect(self.show_on_map)

        view_menu = menubar.addMenu("Ansicht")
        view_menu.addAction(show_on_map_action)

    def create_layout(self):
        self.setWindowTitle("GUI-Programmierung")
        self.setMinimumWidth(600)

        self.firstname_edit = QLineEdit()
        self.lastname_edit = QLineEdit()
        self.birthdate_edit = QDateEdit()
        self.address_edit = QLineEdit()
        self.postalcode_edit = QLineEdit()
        self.location_edit = QLineEdit()
        self.country_combo = QComboBox()
        self.country_combo.addItems(["Schweiz", "Deutschland", "Östereich"])

        show_on_map_button = QPushButton("Auf Karte zeigen")
        show_on_map_button.clicked.connect(self.show_on_map)

        load_button = QPushButton("Laden")
        load_button.clicked.connect(self.load)

        save_button = QPushButton("Speichern")
        save_button.clicked.connect(self.save)

        layout = QFormLayout()
        layout.addRow("Vorname:", self.firstname_edit)
        layout.addRow("Name:", self.lastname_edit)
        layout.addRow("Geburtstag:", self.birthdate_edit)
        layout.addRow("Adresse:", self.address_edit)
        layout.addRow("Postleitzahl:", self.postalcode_edit)
        layout.addRow("Ort:", self.location_edit)
        layout.addRow("Land:", self.country_combo)
        layout.addRow(show_on_map_button)
        layout.addRow(load_button)
        layout.addRow(save_button)

        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)
        self.show()

    def show_on_map(self):
        data = [
            self.address_edit.text(),
            self.postalcode_edit.text(),
            self.location_edit.text(),
            self.country_combo.currentText(),
        ]
        query = "+".join([urllib.parse.quote(value) for value in data])
        link = f"https://www.google.ch/maps/place/{query}"
        QDesktopServices.openUrl(QUrl(link))

    def load(self):
        filename, filter = QFileDialog.getOpenFileName(self, "Datei öffnen", "", "CSV (*.csv);;Textdatei (*.txt)")
        if filename != "":
            file = open(filename, "r", encoding="utf-8")
            reader = csv.reader(file, delimiter=",", lineterminator="\n")
            rows = []
            for row in reader:
                rows.append(row)
            if len(rows) != 0 and len(rows[0]) == 7:
                line = rows[0]
                dformat = QLocale().dateFormat(format=QLocale.FormatType.ShortFormat)
                self.firstname_edit.setText(line[0])
                self.lastname_edit.setText(line[1])
                self.birthdate_edit.setDate(QDate.fromString(line[2], dformat))
                self.address_edit.setText(line[3])
                self.postalcode_edit.setText(line[4])
                self.location_edit.setText(line[5])
                self.country_combo.setCurrentText(line[6])
            file.close()

    def save(self):
        data = [
            self.firstname_edit.text(),
            self.lastname_edit.text(),
            self.birthdate_edit.text(),
            self.address_edit.text(),
            self.postalcode_edit.text(),
            self.location_edit.text(),
            self.country_combo.currentText(),
        ]
        filename, filter = QFileDialog.getSaveFileName(self, "Datei speichern", "", "CSV (*.csv);;Textdatei (*.txt)")
        if filename != "":
            file = open(filename, "w", encoding="utf-8")
            writer = csv.writer(file, delimiter=",", lineterminator="\n")
            writer.writerow(data)
            file.close()

    def quit(self):
        self.close()


def main():
    app = QApplication(sys.argv)
    mainwindow = Fenster()
    mainwindow.raise_()
    app.exec_()


if __name__ == '__main__':
    main()
