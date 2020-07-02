#stock.py

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
        
    def cost(self):
        return self.shares * self.price
        
    def sell(self, count):
        if count > self.shares:
            raise NameError(f'Can\'t sell {count}. Shares not enogh')
        self.shares -= count
        
    def __repr__(self):
        return f'Stock(\'{self.name}\', {self.shares:d}, {self.price:0.2f})'    