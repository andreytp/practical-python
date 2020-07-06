#!python3
#report.py


from fileparse import parse_csv
import stock

   
def str_to_date(str):
    import datetime
    return datetime.datetime.strptime(str, '%m/%d/%Y')
    
def str_to_time(str):
    import datetime
    return datetime.datetime.strptime(str, '%I:%M%p')
    
def strdate_to_tuple(strdate):
    return tuple( int(val) for val in strdate.split('/') )
# portfolio = [ { colname: types[index](row[index]) for colname, index in zip(select, indices) } for row in rows ]

def read_portfolio(filename, **opts):
    import os
    from portfolio import Portfolio

    data_path = os.environ['PY_DATA'] + '/' + filename
    
    with open(data_path, 'rt') as source:
        
        portdicts = parse_csv(source, 
                                select=['name','shares','price'], 
                                types=[str,int,float],
                                has_header = True, 
                                **opts)
        return Portfolio([stock.Stock(**portdict) for portdict in portdicts])
    
def read_prices(filename, **opts):
    import os

    data_path = os.environ['PY_DATA'] + '/' + filename
        
    with open(data_path, 'rt') as source:
        return dict(parse_csv(source, types=[str,float], **opts))
        
def calc_actual_cost(portfolio_file, price_file):
    
    price = read_prices(prefix+price_file)
    portfolio = read_portfolio(prefix+portfolio_file)
    
    total_cost = 0.0
    gain_lost = 0.0
    
    for item in portfolio:
        position_cost = item.cost
        position_gain_lost = 0
        if item['name'] in price:
            position_cost = item.shares * price[item.name]
            position_gain_lost = position_cost - item.cost 
        total_cost += position_cost
        gain_lost += position_gain_lost
    
    return total_cost, gain_lost
            
def make_report_data(portfolio, price):
       
    total_cost = 0.0
    gain_lost = 0.0
    stock_list = []
    
    for rowno, item in enumerate(portfolio):
        position_cost = item.cost
        position_gain_lost = 0
        position_price = item.price
        if item.name in price:
            try:
                position_price = price[item.name]
                position_cost = item.shares * position_price
                position_gain_lost = position_cost - item.cost
            except ValueError:
                print(f'Row {rowno}: Bad row {item}')    
        stock_list.append((item.name, 
                        item.shares, 
                        position_price, 
                        position_price - item.price, 
                        position_gain_lost)
                            )     
        total_cost += position_cost
        gain_lost += position_gain_lost
    
    return stock_list, total_cost, gain_lost
    
def print_report(report, total_cost, total_gain_lost, formatter):
    from tableformat import TextTableFormatter 
    
    headers =   ['Name', 
                'Shares', 
                'Price', 
                'Change', 
                'Gain/Lost']

    formatter.headings(headers)
    
    try:
        for row, item in enumerate(report):
            name, shares, price, change, gain_lost = item
            rowdata =  [f'{name}', 
                        f'{shares:d}', 
                        f'{price:0.2f}', 
                        f'{change:0.2f}', 
                        f'{gain_lost:0.2f}']
                        
                      
            if isinstance(formatter, TextTableFormatter):            
                rowdata =  [f'{name:>10s}', 
                            f'{shares:>10d}', 
                            f'{price:>10.2f}', 
                            f'{change:>10.2f}', 
                            f'{gain_lost:>10.2f}']
            formatter.row(rowdata)
    except ValueError:
        print(f'Row {row}: Bad row {item}') 
    
    footers =    ['Total cost', 
                f'{total_cost:>10.2f}', 
                ' '*10, 
                'Gain/lost', 
                f'{total_gain_lost:>10.2f}']
    formatter.footings(footers)

def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''
    
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report, total_cost, total_gain_lost = make_report_data(portfolio, prices)
    from tableformat import create_formatter
    # Print it out
    formatter = create_formatter(fmt)
                
    print_report(report, total_cost, total_gain_lost, formatter)

def main(argv):
    
    arglen = len(argv)
    
    if arglen < 3:
        print(f'Wrong parametrs number, expected 2 or more received {arglen-1}')
        return
    if arglen > 3:    
        portfolio_report(argv[1], argv[2], fmt=argv[3])
    else:
        portfolio_report(argv[1], argv[2])
    
        
        
if __name__ == '__main__':
        import sys
        main(sys.argv)
