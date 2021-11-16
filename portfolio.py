

class Portfolio:
    def __init__(self):
        self._stocks = []

    def buy(self, name, shares, price):
        self.stocks.append((name, shares,price))
    
    def cost(self):
        return sum(shares * price for _, shares, price in self._stocks)
    
