# fileparse.py
import csv

def parse_csv_step0(filename):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)
        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            record = dict(zip(headers, row))
            records.append(record)

    return records
    
def parse_csv_step1(filename, select=None):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            # Filter the row if specific columns were selected
            if indices:
                row = [ row[index] for index in indices ]

            # Make a dictionary
            record = dict(zip(headers, row))
            records.append(record)

    return records
    
def parse_csv_step2(filename, select=None, types=None):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = [headers.index(colname) for colname in headers]

        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            # Filter the row if specific columns were selected
            row = [ row[index] for index in indices ]
            try:
                if types:
                    row = [ fun(value) for value, fun in zip(row, types) ]
            except:
                print(row)
                print(indices)
                print(types)
                break
            
            # Make a dictionary
            record = dict(zip(headers, row))
            records.append(record)

    return records    
    
def parse_csv(filename, select=None, types=None, has_headers=False, delimiter_=','):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter = delimiter_)

        # Read the file headers
        headers = []
        if has_headers:
            headers = next(rows)
            # If a column selector was given, find indices of the specified columns.
            # Also narrow the set of headers used for resulting dictionaries
            indices = [headers.index(colname) for colname in headers]
            if select:
                indices = [headers.index(colname) for colname in select]
                headers = select
            
                

        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            # Filter the row if specific columns were selected
            
            if has_headers:
                row = [ row[index] for index in indices ]
            
                if types:
                    row = [ fun(value) for value, fun in zip(row, types) ]
            
            # Make a dictionary
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
                
                if types:
                    record = tuple(fun(value) for value, fun in zip(row, types))
                
                    
            records.append(record)

    return records