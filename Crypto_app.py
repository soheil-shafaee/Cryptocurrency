from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5 import uic
import sys
from loading import ProgressBar
from main import Main


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.setWindowIcon(QIcon("images/cryptocurrency.png"))
        self.setFixedSize(398, 578)

        # Load UI File
        uic.loadUi("wellcome.ui", self)

        # Our Widgets
        self.start_button = self.findChild(QPushButton, "start_button")
        self.load = None
        self.main = None
        self.start_button.clicked.connect(self.get_start)

        # Display Window
        self.show()

    def get_start(self):
        pass
        # self.load = ProgressBar()
        # self.load.show()
        # self.main = Main()
        # self.close()
        # self.load.close()
        # self.main.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Ui = UI()
    sys.exit(app.exec_())
