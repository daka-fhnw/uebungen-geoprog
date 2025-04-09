import sys

import csv
from PyQt5.QtWidgets import *


class Fenster(QMainWindow):

    def __init__(self):
        super().__init__()
        self.create_menubar()
        self.create_layout()

    def create_menubar(self):
        menubar = self.menuBar()
       
        save_action = QAction("Save", self)
        save_action.triggered.connect(self.save)

        quit_action = QAction("Quit", self)
        quit_action.triggered.connect(self.quit)

        file_menu = menubar.addMenu("File")
        file_menu.addAction(save_action)
        file_menu.addAction(quit_action)

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

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save)

        layout = QFormLayout()
        layout.addRow("Vorname:", self.firstname_edit)
        layout.addRow("Name:", self.lastname_edit)
        layout.addRow("Geburtstag:", self.birthdate_edit)
        layout.addRow("Adresse:", self.address_edit)
        layout.addRow("Postleitzahl:", self.postalcode_edit)
        layout.addRow("Ort:", self.location_edit)
        layout.addRow("Land:", self.country_combo)
        layout.addRow(save_button)

        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)
        self.show()

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
        file = open("save.csv", "w", encoding="utf-8")
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
