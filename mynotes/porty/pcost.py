#!python3
# pcost.py


def portfolio_cost(filename):
    from . import report
    import os
    
    portfolio = report.read_portfolio(filename)
    
    return portfolio.total_cost
    
def main(argv):
    
    if len(argv) != 2:
        return

    print(portfolio_cost(argv[1]))
        
        
if __name__ == '__main__':
        import sys
        main(sys.argv)
