#stock.py


from .typedproperty import *

class Stock:
    
    # __slots__=('name', '_shares', 'price')
    
    name = String('name')
    shares = Integer('shares')
    price = Float('price')
    
    def __init__(self, name, shares, price):
        
        self.name = name
        self.shares = shares
        self.price = price
                
    @property    
    def cost(self):
        return self._shares * self.price
        
    def sell(self, count):
        if count > self._shares:
            raise RuntimeError(f'Can\'t sell {count}. Shares not enogh')
        self._shares -= count
        
    def __repr__(self):
        return f'Stock(\'{self.name}\', {self._shares:d}, {self.price:0.2f})'
