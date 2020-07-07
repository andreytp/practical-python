
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
    
        yield line
            
            
if __name__ == '__main__':
    from . import report

    portfolio = report.read_portfolio('portfolio.csv')

    for line in follow('stocklog.csv'):
        name, price, change = line.split(',')
        if name in portfolio:
            print(f'{name:>10s} {price:>10s} {change:>10s}')