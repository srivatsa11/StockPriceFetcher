from stock import Stock


class Person:
    def __init__(self, name):
        self.name = name
        self.stock_dict = {}

    def add_stock(self, stock_name, quantity):
        self.stock_dict[stock_name] = quantity

    def get_worth_from_stock_inr(self, stock_name):
        stock = Stock(stock_name)
        qty = self.stock_dict.get(stock_name)
        if qty is not None:
            return qty * stock.get_live_price_in_inr()
        else:
            return 0

    def __str__(self):
        return self.name + " is worth  : " + str(self.get_worth_from_stock_inr('ORCL'))


if __name__ == "__main__":
    p = Person('Srivatsa')
    p.add_stock('ORCL', 196)
    print(p)
