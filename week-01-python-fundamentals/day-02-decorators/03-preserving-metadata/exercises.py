"""
================================================================================
 DAY 2 · PART 3 — `@wraps` / PRESERVING METADATA — EXERCISES
================================================================================
 3 exercises. ~10 minutes. Short topic, short drill.
================================================================================
"""

from functools import wraps
import time


# ============================================================================
# A.  SEE THE PROBLEM
# ============================================================================

# ----- Exercise 1 ------------------------------------------------------------
# Run this block as-is. Observe the output.
def bare_timer(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@bare_timer
def greet(name):
    """Greets someone by name."""
    return f"Hello, {name}"

print("Without @wraps:")
print(" __name__:", greet.__name__)   # what prints?
print(" __doc__: ", greet.__doc__)    # what prints?

# My observation: It just prints the name of wrapper function which is of coursr wrapper
# and it prints None, coz that wrapper functoion has not any docstrings


# ============================================================================
# B.  APPLY THE FIX
# ============================================================================

# ----- Exercise 2 ------------------------------------------------------------
# Rewrite the `timer` decorator you wrote earlier, but add @wraps(func) so
# that the decorated function's name and docstring are preserved.
def timer(func):
    # Your code:
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
    """Square a number slowly."""
    time.sleep(0.1)
    return n * n

# Test:
print(slow_square(5))                    # should print "slow_square took X" then 25
print(slow_square.__name__)              # should be "slow_square" not "wrapper"
print(slow_square.__doc__)               # should be the docstring, not None


# ============================================================================
# C.  SMALL CHALLENGE
# ============================================================================

# ----- Exercise 3 ------------------------------------------------------------
# Write a decorator `log_calls` that:
#   - prints "CALL: <funcname>(<args>)" before the call
#   - prints "RETURN: <result>" after the call
#   - uses @wraps so the decorated function's __name__ is preserved
#   - returns the result unchanged
def log_calls(func):
    # Your code:
    @wraps(func)
    def wrapper(*args, **kwargs):
        
        print(f"CALL {func.__name__} {args}")
        result = func(*args, **kwargs)
        print(f"RETURN {result}")
        return result
    return wrapper


@log_calls
def add(a, b):
    """Adds two numbers."""
    return a + b

# Test:
print(add(3, 4))
# expected:
#   CALL: add((3, 4))
#   RETURN: 7
#   7
# print(add.__name__)    # "add"
# print(add.__doc__)     # "Adds two numbers."

