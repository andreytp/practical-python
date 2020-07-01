# pcost.py
import report


def portfolio_cost(filename):
    
    portfolio = report.read_portfolio(filename)
    
    return sum([item['shares'] * item['price'] for item in portfolio])
    