from yahoo_fin import stock_info as si
from forex_python.converter import CurrencyRates
import time

class Stock:
    def __init__(self, name):
        self.name = name

    def get_live_price(self):
        return si.get_live_price(self.name)

    def get_live_price_in_inr(self):
        c = CurrencyRates()
        return c.convert('USD', 'INR', self.get_live_price())

    def __str__(self):
        return self.name + " : " + str(self.get_live_price())


if __name__ == "__main__":
    oracle_stock = Stock('ORCL')
    while True:
        print(oracle_stock)
        time.sleep(5)


