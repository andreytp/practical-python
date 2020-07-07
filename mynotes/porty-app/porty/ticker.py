#ticker.py

from .follow import follow
import csv

def convert_types(rows, indices):
     # "CAT",78.55,"6/11/2007","11:00.51",0.03,78.32,78.88,77.99,920639
    funs = [str, float, str, str, float, float, float, float, int]
    return ( (fun(val) for fun, val in zip((funs[i] for i in indices), row)) for row in rows)
        
def get_names(indices):
    names = ['name','price','date','time','change','open','high','low','volume']
    return (names[i] for i in indices)
    

def make_dicts(rows, indices):
    selectnames = get_names(indices)
    return (dict(zip(selectnames, row)) for row in rows)
        
def make_stocks(rows, indices):
    
    from .stock import Stock
    for row in rows:
        selectnames = get_names(indices)
        fieldname = next(selectnames)    
        stockname = next(row)
        stock_item = Stock(stockname,0,0)
        for name, val in zip(selectnames, row):
            setattr(stock_item, name, val)
        yield stock_item


def select_columns(rows, indices):
    return ( (row[index] for index in indices) for row in rows )

def get_portfolio_symbols():
    from . import report
    portfolio = report.read_portfolio('portfolio.csv')
    return list(set(item.name for item in portfolio))
    

def parse_stock_data(lines, indices):
    symbols = get_portfolio_symbols()
    rows = csv.reader(lines)
    rows = select_columns(rows, indices)
    rows = convert_types(rows, indices)
    rows = make_stocks(rows, indices)
    rows = filter_symbols(rows, symbols)
    return rows
    
def filter_symbols(rows, symbols):
    return (row for row in rows if row.name in symbols)
            
def ticker(fmt):
    import sys
    argv = sys.argv
    
    indices = [i for i in range(9)]
    
    if len(argv) > 1:
        indices = [int(arg) for arg in argv[1:]]
        
    lines = follow('stocklog.csv')
    rows = parse_stock_data(lines, indices)
    
    from .tableformat import create_formatter
    from .tableformat import print_table
    
    formatter = create_formatter(fmt)
    print_table(rows, list(get_names(indices)), formatter)
        
    
if __name__ == '__main__':
    ticker('txt')
#python3 ticker.py 0 1 4 6 8