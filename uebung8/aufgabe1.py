
import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Polynomfunktion")

        layout = QVBoxLayout()
        self.plotlayout(layout)
        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)
        self.show()

        self.apply_action()

    def plotlayout(self, layout):
        figure = plt.figure(figsize=(8, 5))
        self.canvas = FigureCanvas(figure)

        self.coeff_edit = QLineEdit()
        self.coeff_edit.setText("2, 3, 4")

        self.minimum_edit = QLineEdit()
        self.minimum_edit.setText('0')

        self.maximum_edit = QLineEdit()
        self.maximum_edit.setText('10')

        self.ptcount_edit = QSpinBox()
        self.ptcount_edit.setValue(20)
        self.ptcount_edit.setMinimum(2)
        self.ptcount_edit.setMaximum(99)

        self.color_combo = QComboBox()
        self.color_combo.addItem("red")
        self.color_combo.addItem("green")
        self.color_combo.addItem("blue")
        self.color_combo.addItem("cyan")
        self.color_combo.addItem("magenta")
        self.color_combo.addItem("yellow")
        self.color_combo.addItem("black")
        self.color_combo.currentIndexChanged.connect(self.redraw_plot)

        apply_button = QPushButton("Anwenden")
        apply_button.clicked.connect(self.apply_action)

        line_layout1 = QHBoxLayout()
        line_layout1.addWidget(QLabel("Koeffizienten:"))
        line_layout1.addWidget(self.coeff_edit)

        line_layout2 = QHBoxLayout()
        line_layout2.addWidget(QLabel("Minimum:"))
        line_layout2.addWidget(self.minimum_edit)
        line_layout2.addWidget(QLabel("Maximum:"))
        line_layout2.addWidget(self.maximum_edit)
        line_layout2.addWidget(QLabel("Anzahl Punkte:"))
        line_layout2.addWidget(self.ptcount_edit)
        line_layout2.addWidget(QLabel("Plotfarbe:"))
        line_layout2.addWidget(self.color_combo)

        layout.addLayout(line_layout1)
        layout.addLayout(line_layout2)
        layout.addWidget(apply_button)
        layout.addWidget(self.canvas)

    def apply_action(self):
        self.build_function()
        self.build_values()
        self.redraw_plot()

    def build_function(self):
        text = self.coeff_edit.text()
        try:
            coeff = [int(value.strip())
                     for value in text.split(",") if value != ""]
            if len(coeff) < 1:
                raise ValueError("no coefficients")
            self.fun = np.poly1d(coeff)
            self.show_invalid(self.coeff_edit, False)
        except ValueError:
            self.fun = None
            self.show_invalid(self.coeff_edit, True)

    def build_values(self):
        try:
            minimum = float(self.minimum_edit.text())
            self.show_invalid(self.minimum_edit, False)
        except ValueError:
            minimum = None
            self.show_invalid(self.minimum_edit, True)
        try:
            maximum = float(self.maximum_edit.text())
            if maximum < minimum:
                raise ValueError('maximum < minimum')
            self.show_invalid(self.maximum_edit, False)
        except ValueError:
            maximum = None
            self.show_invalid(self.maximum_edit, True)
        try:
            ptcount = int(self.ptcount_edit.text())
            if ptcount < 2:
                raise ValueError('ptcount < 2')
            self.show_invalid(self.ptcount_edit, False)
        except ValueError:
            ptcount = None
            self.show_invalid(self.ptcount_edit, True)
        if minimum != None and maximum != None and ptcount != None:
            self.values = np.linspace(minimum, maximum, ptcount)
        else:
            self.values = []

    def redraw_plot(self):
        plt.clf()
        if self.fun != None and len(self.values) != 0:
            x = np.array(self.values)
            y = self.fun(x)
            c = self.color_combo.currentText()
            plt.plot(x, y, "o-", color=c)
            self.canvas.draw()

    def show_invalid(self, line_edit, value):
        if value:
            line_edit.setStyleSheet("border: 2px solid red;")
        else:
            line_edit.setStyleSheet("")


def main():
    app = QApplication(sys.argv)
    mainwindow = Window()
    mainwindow.raise_()
    app.exec_()


if __name__ == '__main__':
    main()
