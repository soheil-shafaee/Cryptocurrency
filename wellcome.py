from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QIcon
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.setWindowIcon(QIcon("images/cryptocurrency.png"))

        # Load UI File
        uic.loadUi("wellcome.ui", self)

        # Our Widgets
        self.wellcome_text = self.findChild(QLabel, "welcome_text")
        self.app_name = self.findChild(QLabel, "app_name")

        # Display Window
        self.show()


app = QApplication(sys.argv)
Ui = UI()
app.exec_()