from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QComboBox
from PyQt5 import uic
import sys
import requests


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()

        # Load UI File
        uic.loadUi("main.ui", self)
        # Fixed Window
        self.setFixedSize(398, 578)

        # Define Our Widgets
        self.coin_price_list = []
        self.coin_percent = []
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

        self.units_list.addItems(["", "USD", "EUR"])
        self.units_list.currentTextChanged.connect(self.update_units)

        self.get_price()

        # Display Window
        self.show()

    def update_units(self, text):
        if text == "USD":
            self.unit1.setText("$")
            self.btc_price.setText(str(f"{self.coin_price_list[0]['USD']:,}"))
            self.unit2.setText("$")
            self.eth_price.setText(str(f"{self.coin_price_list[1]['USD']:,}"))
            self.unit3.setText("$")
            self.sol_price.setText(str(f"{self.coin_price_list[2]['USD']:,}"))
            self.unit4.setText("$")
            self.doge_price.setText(str(f"{self.coin_price_list[3]['USD']:,}"))
            self.unit5.setText("$")
            self.usdt_price.setText(str(f"{self.coin_price_list[4]['USD']:,}"))

        elif text == "EUR":
            self.unit1.setText("€")
            self.btc_price.setText(str(f"{self.coin_price_list[0]['EUR']:,}"))
            self.unit2.setText("€")
            self.eth_price.setText(str(f"{self.coin_price_list[1]['EUR']:,}"))
            self.unit3.setText("€")
            self.sol_price.setText(str(f"{self.coin_price_list[2]['EUR']:,}"))
            self.unit4.setText("€")
            self.doge_price.setText(str(f"{self.coin_price_list[3]['EUR']:,}"))
            self.unit5.setText("€")
            self.usdt_price.setText(str(f"{self.coin_price_list[4]['EUR']:,}"))
        if "-" in self.coin_percent[0]:
            self.btc_percent.setStyleSheet("color: rgb(191, 1, 1)")
        self.btc_percent.setText(self.coin_percent[0] + "%")

        if "-" in self.coin_percent[1]:
            self.eth_percent.setStyleSheet("color: rgb(191, 1, 1)")
        self.eth_percent.setText(self.coin_percent[1] + "%")

        if "-" in self.coin_percent[2]:
            self.sol_percent.setStyleSheet("color:  rgb(191, 1, 1)")
        self.sol_percent.setText(self.coin_percent[2] + "%")

        if "-" in self.coin_percent[3]:
            self.doge_percent.setStyleSheet("color:  rgb(191, 1, 1)")
        self.doge_percent.setText(self.coin_percent[3] + "%")

        if "-" in self.coin_percent[4]:
            self.usdt_percent.setStyleSheet("color:  rgb(191, 1, 1)")
        self.usdt_percent.setText(self.coin_percent[4] + "%")

    def get_price(self):
        coin_list = ["BTC", "ETH", "SOL", "DOGE", "USDT"]

        for coin in coin_list:
            response = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={coin}&tsyms=USD,JPY,EUR")
            response_percent = requests.get(
                f"https://min-api.cryptocompare.com/data/pricemultifull?fsyms={coin}&tsyms=USD")
            percent = response_percent.json()["DISPLAY"][f"{coin}"]["USD"]["CHANGEPCT24HOUR"]
            self.coin_percent.append(percent)
            self.coin_price_list.append(response.json())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    app.exec_()
