#!python3
# pcost.py


def portfolio_cost(filename):
    import report
    import os
    
    portfolio = report.read_portfolio(filename)
    
    return sum([item.cost() for item in portfolio])
    
def main(argv):
    
    if len(argv) != 2:
        return

    print(portfolio_cost(argv[1]))
        
        
if __name__ == '__main__':
        import sys
        main(sys.argv)
