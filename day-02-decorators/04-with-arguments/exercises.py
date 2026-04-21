"""
================================================================================
 DAY 2 · PART 4 — DECORATORS WITH ARGUMENTS — EXERCISES
================================================================================
 4 exercises. ~45 minutes. Progressive difficulty.

 The three-layer skeleton to memorize:

     def decorator_factory(arg1, arg2):       # Layer 1 — the arguments
         def decorator(func):                  # Layer 2 — the function
             @wraps(func)
             def wrapper(*args, **kwargs):    # Layer 3 — the call arguments
                 # use arg1, arg2, func here
                 return func(*args, **kwargs)
             return wrapper
         return decorator

 Three names, three returns. Read bottom-up.
================================================================================
"""

from functools import wraps
import time
import random


# ============================================================================
# A.  WARMUP — READ BEFORE YOU WRITE
# ============================================================================

# ----- Exercise 1 ------------------------------------------------------------
# Read this code. Without running it, predict what prints.
def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hi(name):
    print(f"Hi, {name}!")
    return "done"

# result = say_hi("Alice")
# print("Returned:", result)
#
# My prediction (4 lines of output): 
# Hi, Alice
# Hi, Alice
# Hi, Alice
# Returned: done


# ============================================================================
# B.  WRITE YOUR FIRST
# ============================================================================

# ----- Exercise 2 ------------------------------------------------------------
# Write a decorator `prefix(text)` that prepends `text + ": "` to the return
# value of the wrapped function. Assume the function returns a string.
def prefix(text):
    # Your code:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return text + ": " + result
        return wrapper
    return decorator

@prefix("INFO")
def get_message():
    return "server started"

@prefix("WARNING")
def get_alert():
    return "disk almost full"

# Test:
print(get_message())     # "INFO: server started"
print(get_alert())       # "WARNING: disk almost full"


# ============================================================================
# C.  THE @retry DELIVERABLE
# ============================================================================

# ----- Exercise 3 ------------------------------------------------------------
# Write a decorator `@retry(max_attempts, delay)` that:
#   - calls the wrapped function
#   - if it raises an exception, waits `delay` seconds and tries again
#   - gives up after `max_attempts` total attempts
#   - on final failure, re-raises the last exception
#   - prints which attempt is being tried, like "Attempt 1/3..."
#
# Use time.sleep(delay) to wait between attempts.
# Use @wraps(func).
def retry(max_attempts, delay):
    # Your code:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                print(f"Attempt {attempt}/{max_attempts}...")
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts:
                        time.sleep(delay)
            
            raise last_exception
        return wrapper
    return decorator



# A flaky function for testing — fails 2 times then succeeds
_call_count = {"flaky": 0}

@retry(max_attempts=3, delay=0.1)
def flaky_function():
    _call_count["flaky"] += 1
    if _call_count["flaky"] < 3:
        raise ValueError(f"Attempt failed ({_call_count['flaky']})")
    return "success!"

# Test:
print(flaky_function())
# expected output:
#   Attempt 1/3...
#   Attempt 2/3...
#   Attempt 3/3...
#   success!


# ----- Exercise 3b — test the failure case ----------------------------------
# This function ALWAYS fails. Your @retry should retry 3 times, then give up
# and re-raise the exception. Make sure your decorator handles that.

@retry(max_attempts=3, delay=0.05)
def always_fails():
    raise RuntimeError("I never work")

# Test (wrap in try/except to see it):
try:
    always_fails()
except RuntimeError as e:
    print(f"Finally gave up after 3 tries: {e}")


# ============================================================================
# D.  ONE MORE — A RANGE-ENFORCING DECORATOR (challenge)
# ============================================================================

# ----- Exercise 4 ------------------------------------------------------------
# Write a decorator `@in_range(low, high)` that ensures the wrapped function's
# return value is between `low` and `high` (inclusive). If it's outside the
# range, raise ValueError. Otherwise return the value unchanged.
def in_range(low, high):
    # Your code:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if low <= result <= high:
                return result
            else:
                raise ValueError
        return wrapper
    return decorator
            

@in_range(0, 100)
def get_score():
    return 85

@in_range(0, 100)
def get_bad_score():
    return 150

# Test:
print(get_score())           # 85
try:
    get_bad_score()
except ValueError as e:
    print(f"Caught: {e}")    # some message about 150 being out of range

