#tymethis.py

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('%s.%s: %f' % (func.__module__, func.__name__, end-start))
        return result, end-start
    return wrapper    