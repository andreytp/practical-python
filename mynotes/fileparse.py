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
    
def parse_csv_step3(filename, select=None, types=None, has_headers=False, delimiter_=','):
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
    
def parse_csv_step4(filename, select=None, types=None, has_headers=False, delimiter_=','):
    '''
    Parse a CSV file into a list of records
    '''
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")
    
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
        
def parse_csv_step5(filename, select=None, types=None, has_headers=False, delimiter_=','):
    '''
    Parse a CSV file into a list of records
    '''
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")
    
    with open(filename) as f:
        rows = csv.reader(f, delimiter = delimiter_)

        # Read the file headers
        headers = []
        startrow = 0
        if has_headers:
            headers = next(rows)
            # If a column selector was given, find indices of the specified columns.
            # Also narrow the set of headers used for resulting dictionaries
            startrow = 1
            indices = [headers.index(colname) for colname in headers]
            if select:
                indices = [headers.index(colname) for colname in select]
                headers = select
            
        records = []
        for rowno, row in enumerate(rows, start = startrow):
            if not row:    # Skip rows with no data
                continue
            # Filter the row if specific columns were selected
            
            if has_headers:
                row_typed = [ row[index] for index in indices ]
            
                if types:
                    try:
                        row_typed = [ fun(value) for value, fun in zip(row, types) ]
                    except ValueError as e:
                        print(f'Row {rowno}: Couldn\'t convert {row}')
                        print(f'Row {rowno}: Reason: {e}')
                        continue 
            
            # Make a dictionary
                record = dict(zip(headers, row_typed))
            else:
                record = tuple(row)
                
                if types:
                    try:
                        record = tuple(fun(value) for value, fun in zip(row, types))
                    except ValueError as e:
                        print(f'Row {rowno}: Couldn\'t convert {row}')
                        print(f'Row {rowno}: Reason: {e}')
                        continue
                
                    
            records.append(record)

    return records

def parse_csv_step6(filename, select=None, types=None, has_headers=False, silence_errors=True, delimiter_=','):
    '''
    Parse a CSV file into a list of records
    '''
    
    import os
    
    data_path = os.environ['PY_DATA'] + '/' + filename
    
    
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")
    
    with open(data_path) as f:
        rows = csv.reader(f, delimiter = delimiter_)

        # Read the file headers
        headers = []
        startrow = 0
        if has_headers:
            headers = next(rows)
            # If a column selector was given, find indices of the specified columns.
            # Also narrow the set of headers used for resulting dictionaries
            startrow = 1
            indices = [headers.index(colname) for colname in headers]
            if select:
                indices = [headers.index(colname) for colname in select]
                headers = select
            
        records = []
        for rowno, row in enumerate(rows, start = startrow):
            if not row:    # Skip rows with no data
                continue
            # Filter the row if specific columns were selected
            
            if has_headers:
                row_typed = [ row[index] for index in indices ]
            
                if types:
                    try:
                        row_typed = [ fun(value) for value, fun in zip(row, types) ]
                    except ValueError as e:
                        if not silence_errors:
                            print(f'Row {rowno}: Couldn\'t convert {row}')
                            print(f'Row {rowno}: Reason: {e}')
                        continue 
            
            # Make a dictionary
                record = dict(zip(headers, row_typed))
            else:
                record = tuple(row)
                
                if types:
                    try:
                        record = tuple(fun(value) for value, fun in zip(row, types))
                    except ValueError as e:
                        if not silence_errors:
                            print(f'Row {rowno}: Couldn\'t convert {row}')
                            print(f'Row {rowno}: Reason: {e}')
                        continue
                
                    
            records.append(record)

    return records
    
def parse_csv(source, select=None, types=None, **opts ):
    '''
    Parse a CSV file into a list of records
    '''
    has_headers=False
    silence_errors=True
    delimiter_=','
    
    if 'has_header' in opts.keys():
        has_headers = opts['has_header']
        
    if 'silence_errors' in opts.keys():
        silence_errors = opts['silence_errors']
        
    if 'delimiter' in opts.keys():
        delimiter = opts['delimiter']
        
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")

    rows = csv.reader(source, delimiter = delimiter_)

        # Read the file headers
    headers = []
    startrow = 0
    if has_headers:
        headers = next(rows)
        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        startrow = 1
        indices = [headers.index(colname) for colname in headers]
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        
    records = []
    for rowno, row in enumerate(rows, start = startrow):
        if not row:    # Skip rows with no data
            continue
        # Filter the row if specific columns were selected
        
        if has_headers:
            row_typed = [ row[index] for index in indices ]
        
            if types:
                try:
                    row_typed = [ fun(value) for value, fun in zip(row, types) ]
                except ValueError as e:
                    if not silence_errors:
                        print(f'Row {rowno}: Couldn\'t convert {row}')
                        print(f'Row {rowno}: Reason: {e}')
                    continue 
        
        # Make a dictionary
            record = dict(zip(headers, row_typed))
        else:
            record = tuple(row)
            
            if types:
                try:
                    record = tuple(fun(value) for value, fun in zip(row, types))
                except ValueError as e:
                    if not silence_errors:
                        print(f'Row {rowno}: Couldn\'t convert {row}')
                        print(f'Row {rowno}: Reason: {e}')
                    continue
            
                
        records.append(record)

    return records        