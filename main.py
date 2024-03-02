from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QComboBox
from PyQt5 import uic
import sys


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()

        # Load UI File
        uic.loadUi("main.ui", self)
        # Fixed Window
        self.setFixedSize(398, 578)

        # Define Our Widgets
        self.units_list = self.findChild(QComboBox, "units_list")
        self.unit1 = self.findChild(QLabel, "units1")
        self.btc_price = self.findChild(QLabel, "btc_price")
        self.btc_percent = self.findChild(QLabel, "btc_percent")
        self.unit2 = self.findChild(QLabel, "units2")
        self.eth_price = self.findChild(QLabel, "eth_price")
        self.eth_percent = self.findChild(QLabel, "eth_percent")
        self.unit3 = self.findChild(QLabel, "units3")
        self.sol_price = self.findChild(QLabel, "sol_price")
        self.sol_percent = self.findChild(QLabel, "sol_percent")
        self.unit4 = self.findChild(QLabel, "units4")
        self.doge_price = self.findChild(QLabel, "doge_price")
        self.doge_percent = self.findChild(QLabel, "doge_percent")
        self.unit5 = self.findChild(QLabel, "units5")
        self.usdt_price = self.findChild(QLabel, "usdt_price")
        self.usdt_percent = self.findChild(QLabel, "usdt_percent")

        # Display Window
        self.show()


app = QApplication(sys.argv)
main = Main()
app.exec_()
