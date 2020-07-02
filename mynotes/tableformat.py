#tableformat.py

from exceptions import FormatError

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()
        
    def row(self, rowdata):
        '''
        Emit a singl row of table data
        '''
        raise NotImplementedError()
        
    def footings(self, footers):
        '''   
        Emit the table headings.
        '''
        raise NotImplementedError()
        
class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        for h in headers:
            print(f'{h:10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))
        
    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()
        
    def footings(self, footers):
        print(('-'*10 + ' ')*len(footers))
        for f in footers:
            print(f'{f:10s}', end=' ')
        print()
    
class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))
        
    def footings(self, footers):
         print()
         
class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>')
        for h in headers:
            print(f'<th>{h:s}</th>', end='')
        print('</tr>')
                
    def row(self, rowdata):
        print('<tr>')
        for d in rowdata:
            print(f'<td>{d:s}</td>', end='')
        print('</tr>')
        
    def footings(self, footers):
        print('<tr>')
        for f in footers:
            print(f'<th>{f:s}</th>', end='')
        print('</tr>')
        
def create_formatter(fmt):
    if fmt == 'txt':
        formatter = TextTableFormatter()
    elif fmt == 'csv':
        formatter = CSVTableFormatter()
    elif fmt == 'html':
        formatter = HTMLTableFormatter()
    else:
        raise FormatError(f'Unknow format {fmt}')
    return formatter
    
def print_table(collection, fields, formatter):
    
    formatter.headings(fields)
    for item in collection:
        rowdata = []
        # print(item)
        for field in fields:
            strval = value_format(getattr(item, field))
            # print(strval)
            rowdata.append(strval)
        formatter.row(rowdata)
        
def value_format(value):
    if isinstance(value, int):
        return f'{value:>10d}'
        
    if isinstance(value, float):
        return f'{value:>10.2f}'
        
    return f'{value:>10s}'
        
    
    