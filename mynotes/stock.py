#stock.py

class Stock:
    
    __slots__=('name', '_shares', 'price')
    
    def __init__(self, name, shares, price):
        self.name = name
        self._shares = shares
        # SELFSET_shares(shares)

        self.price = price
        
    # Function that layers the "get" operation
    @property
    def shares(self):
        return self._shares

    # Function that layers the "set" operation
    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        self._shares = value
        
    @shares.deleter
    def shares(self):
        raise RuntimeError('Don\'t delete shares property!')
        
    @property    
    def cost(self):
        return self._shares * self.price
        
    def sell(self, count):
        if count > self._shares:
            raise RuntimeError(f'Can\'t sell {count}. Shares not enogh')
        self._shares -= count
        
    def __repr__(self):
        return f'Stock(\'{self.name}\', {self._shares:d}, {self._price:0.2})'    