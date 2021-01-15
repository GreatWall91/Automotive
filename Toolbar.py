import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QToolBar, QAction, QStatusBar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("app")

        label = QLabel("diocane")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("ciao")
        self.addToolBar(toolbar)

        buttonaction = QAction("BUTTON", self)
        buttonaction.setStatusTip("boh")
        buttonaction.triggered.connect(self.azione)
        buttonaction.setCheckable(True)
        toolbar.addAction(buttonaction)

        self.setStatusBar(QStatusBar(self))

    def azione(self, s):
        print("click", s)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()