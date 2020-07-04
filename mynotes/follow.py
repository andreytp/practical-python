
#follow.py

import os
import time


def follow(filename):
    f = open('../Work/Data/'+ filename)
    f.seek(0, os.SEEK_END)

    # names = set()

    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.5)
            continue
    
        # fields = line.split(',')
        # name = fields[0].strip('"')
        # price = float(fields[1])
        # change = float(fields[4])
        # if change < 0:
            # print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
            # names.add(name)
            # yield f'{name:s},{price:>0.2f},{change:>0.2f}'
        yield line
            
            
if __name__ == '__main__':
    import report

    portfolio = report.read_portfolio('portfolio.csv')

    for line in follow('stocklog.csv'):
        name, price, change = line.split(',')
        if name in portfolio:
            print(f'{name:>10s} {price:>10s} {change:>10s}')