#!python3
#report.py


from fileparse import parse_csv


def read_portfolio_tuple(filename):
    
    portfolio = []
    
    if len(filename) == 0:
        return portfolio
        
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
    
    return portfolio
    
def read_portfolio(filename):
        
    return parse_csv(filename, select=['name','shares','price'], types=[str,int,float], has_headers = True)
    
def read_prices(filename):
        
    return dict(parse_csv(filename, types=[str,float]))
        
def calc_actual_cost(portfolio_file, price_file, prefix = '../Work/Data/'):
    
    price = read_prices(prefix+price_file)
    portfolio = read_portfolio(prefix+portfolio_file)
    
    total_cost = 0.0
    gain_lost = 0.0
    
    for item in portfolio:
        position_cost = item['shares'] * item['price']
        position_gain_lost = 0
        if item['name'] in price:
            position_cost = item['shares'] * price[item['name']]
            position_gain_lost = position_cost - item['shares'] * item['price'] 
        total_cost += position_cost
        gain_lost += position_gain_lost
    
    return total_cost, gain_lost
            
def make_report(portfolio, price):
       
    total_cost = 0.0
    gain_lost = 0.0
    stock_list = []
    stock_list.append(('Name', 'Shares', 'Price', 'Change', 'Gain/Lost'))
    stock_list.append(('----------', '----------', '----------', '----------', '----------'))
    
    for rowno, item in enumerate(portfolio):
        position_cost = item['shares'] * item['price']
        position_gain_lost = 0
        position_price = item['price']
        if item['name'] in price:
            try:
                position_price = price[item['name']]
                position_cost = item['shares'] * position_price
                position_gain_lost = position_cost - item['shares'] * item['price']
            except ValueError:
                print(f'Row {rowno}: Bad row {item}')    
        stock_list.append((item['name'], 
                        item['shares'], 
                        position_price, 
                        position_price - item['price'], 
                        position_gain_lost)
                            )     
        total_cost += position_cost
        gain_lost += position_gain_lost
    stock_list.append(('----------', '----------', '----------', '----------', '----------'))
    stock_list.append(('Total cost', total_cost, '----------', 'Gain/Lost ', gain_lost))
    return stock_list
    
def print_report(report):
    len_report = len(report)
    row0 = report[0]
    print(f'{row0[0]:>10s} {row0[1]:>10s} {row0[2]:>10s} {row0[3]:>10s} {row0[4]:>10s}')
    row0 = report[1]
    print(f'{row0[0]:>10s} {row0[1]:>10s} {row0[2]:>10s} {row0[3]:>10s} {row0[4]:>10s}')

    try:
        for row, item in enumerate(report):
            if row < 2:
                continue
            
            if row == len_report-2:
                break
                
            name, shares, price, change, gain_lost = item
            print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f} {gain_lost:>10.2f}')
    except ValueError:
        print(f'Row {row}: Bad row {item}') 
            
    row0 = report[len_report - 2]
    print(f'{row0[0]:>10s} {row0[1]:>10s} {row0[2]:>10s} {row0[3]:>10s} {row0[4]:>10s}')
    
    row0 = report[len_report - 1]
    print(f'{row0[0]:>10s} {row0[1]:>10.2f} {row0[2]:>10s} {row0[3]:>10s} {row0[4]:>10.2f}')
   

    
def str_to_date(str):
    import datetime
    return datetime.datetime.strptime(str, '%m/%d/%Y')
    
def str_to_time(str):
    import datetime
    return datetime.datetime.strptime(str, '%I:%M%p')
    
def strdate_to_tuple(strdate):
    return tuple( int(val) for val in strdate.split('/') )
# portfolio = [ { colname: types[index](row[index]) for colname, index in zip(select, indices) } for row in rows ]

def main(argv):
    
    if len(argv) != 3:
        print(f'Wrong parametrs number, expected 2 received {len(argv)-1}')
        return

    print_report(make_report(read_portfolio(argv[1]), read_prices(argv[2])))
    
        
        
if __name__ == '__main__':
        import sys
        main(sys.argv)
