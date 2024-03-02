from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.setWindowIcon(QIcon("images/cryptocurrency.png"))
        self.setFixedSize(398, 578)

        # Load UI File
        uic.loadUi("wellcome.ui", self)

        # Our Widgets
        self.start_button = self.findChild(QPushButton, "")

        # Display Window
        self.show()


app = QApplication(sys.argv)
Ui = UI()
app.exec_()