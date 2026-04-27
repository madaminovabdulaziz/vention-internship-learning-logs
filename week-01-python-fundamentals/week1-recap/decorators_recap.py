import time
from functools import wraps


def retry(max_attempts, delay):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                print(f"Attemt {attempt}/{max_attempts}...")
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts:
                        time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator




def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(f'Function {func.__name__} took {end - start:.4f} seconds to execute')
        return result
    return wrapper


@retry(max_attempts=3, delay=3)
@timer
def adder(a, b):
    """
    Just addder
    """
    return a + b


print(adder(2, 5))

print(adder.__name__)
print(adder.__doc__)