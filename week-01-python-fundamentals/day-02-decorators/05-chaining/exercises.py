from functools import wraps
import time
from typing import List



def log_calls(func):
    # Your code:
    @wraps(func)
    def wrapper(*args, **kwargs):
        
        print(f"CALL {func.__name__} {args}")
        result = func(*args, **kwargs)
        print(f"RETURN {result}")
        return result
    return wrapper


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} took {end - start:.4f} seconds of time!")
        return result
    return wrapper


@log_calls
@timer
def two_sum(nums: List, target: int):
    prevMap = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i


nums = [1, 2, 3, 4, 5, 6]
target = 7

print(two_sum(nums, target))







