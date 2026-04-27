import time
from functools import wraps



def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds!")
        return result
    return wrapper


@timer
def slow_square(n):
    """
    Square a number only!
    """
    time.sleep(2)
    return n * n

print(slow_square.__name__) # wrapper 
print(slow_square.__doc__) # None


