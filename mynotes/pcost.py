#!python3
# pcost.py


def portfolio_cost(filename):
    import report
    import os
    
    data_path = os.environ['PY_DATA'] + '/' + filename
    portfolio = report.read_portfolio(data_path)
    
    return sum([item['shares'] * item['price'] for item in portfolio])
    
def main(argv):
    
    if len(argv) != 2:
        return

    print(portfolio_cost(argv[1]))
        
        
if __name__ == '__main__':
        import sys
        main(sys.argv)
