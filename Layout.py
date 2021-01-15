import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QTabWidget, QWidget

from LayoutColor import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("app")

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.North)
        tabs.setMovable(True)

        for n, color in enumerate(["red", "blue", "green", "brown"]):
            tabs.addTab(Color(color), color)

        tabs.setTabEnabled(2, False)

        self.setCentralWidget(tabs)




app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()