# fileparse.py
import csv
import logging
log = logging.getLogger(__name__)
   
def parse_csv(source, select=None, types=None, **opts ):
    '''
    Parse a CSV file into a list of records
    '''
    has_headers=False
    silence_errors=True
    delimiter_=','
    
    if 'has_headers' in opts:
        has_headers = opts['has_headers']
        
    if 'silence_errors' in opts:
        silence_errors = opts['silence_errors']
        
    if 'delimiter' in opts:
        delimiter = opts['delimiter']
        
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")

    rows = csv.reader(source, delimiter = delimiter_)

        # Read the file headers
    headers = []
    startrow = 0
    indices = None
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
        row_filtered = row
        
        if indices:
            row_filtered = [ row[index] for index in indices ]
    
        row_typed = row_filtered
        
        if types:
            try:
                row_typed = [ fun(value) for value, fun in zip(row_filtered, types) ]
            except ValueError as e:
                if not silence_errors:
                    log.warning(f'Row {rowno}: Couldn\'t convert {row}')
                    log.debug(f'Row {rowno}: Reason: {e}')
                continue 
        
        record = tuple(row_typed)
        if has_headers:
        # Make a dictionary
            record = dict(zip(headers, row_typed))

        records.append(record)

    return records