import os
import sys
import csv

os.chdir('/Users/andreytp/practical-python/Work')

def portfolio_cost(filename):
    sum = 0
    try:
        f = open(filename)
        rows = csv.reader(f)
        headers = next(rows)
        for i,row in enumerate(rows):
            if len(row[1]) == 0 or len(row[2]) == 0:
                print(f'Row {i}: Couldn\'t convert: {row}')
                continue 
            sum =  sum + int(row[1]) * float(row[2])
    except:
        print(sys.exc_info())
        print(f"File {filename} not found")
        sum = 0
    
    finally:
        f.close()
        return sum
        
filename = "Data/portfolio.csv"
if len(sys.argv) == 2:
    filename = sys.argv[1]
           
print(f'Total cost = {portfolio_cost(filename):.2f}')
        
        