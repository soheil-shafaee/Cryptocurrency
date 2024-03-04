from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QProgressBar
from PyQt5.QtGui import QIcon
from PyQt5 import uic
import sys
from main import Main
import time

TIME_LIMIT = 100


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.setWindowIcon(QIcon("images/cryptocurrency.png"))
        self.setFixedSize(398, 578)

        # Load UI File
        uic.loadUi("wellcome.ui", self)

        # Our Widgets
        self.main = None
        self.start_button = self.findChild(QPushButton, "start_button")
        self.progress = self.findChild(QProgressBar, "progressBar")

        self.progress.setValue(0)
        self.progress.setMaximum(100)

        self.start_button.clicked.connect(self.get_start)

        # Display Window
        self.show()

    def get_start(self):
        count = 0
        while count < TIME_LIMIT:
            count += 10
            time.sleep(1)
            self.progress.setValue(count)
            if count == 90:
                self.main = Main()
        self.main.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Ui = UI()
    sys.exit(app.exec_())
