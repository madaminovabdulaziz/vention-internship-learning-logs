"""
================================================================================
 DAY 2 · PART 2 — DECORATOR BASICS — EXERCISES
================================================================================
 5 exercises. ~45 minutes. Predict, then run.

 Remember the skeleton:

     def decorator(func):
         def wrapper(*args, **kwargs):
             # do something before
             result = func(*args, **kwargs)
             # do something after
             return result
         return wrapper

 If you get UnboundLocalError or "NoneType has no 'call'" — you probably
 forgot a `return`. Re-read the skeleton.
================================================================================
"""

# ============================================================================
# A.  SEE IT WITHOUT MAGIC FIRST
# ============================================================================

# ----- Exercise 1 ------------------------------------------------------------
# The @ syntax is sugar. Write the manual equivalent of this:
#
# @shout
# def greet():
#     return "hello"
#
# In the space below, WITHOUT using @, write the two lines that accomplish
# the same thing. (Hint: define greet normally, then reassign it through shout.)

def shout(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

# Your two lines — no @ allowed:
# (1) define greet
# (2) reassign greet through shout

def greet():
    return "Hello"

greet = shout(greet)


# Test:
# print(greet())   # should print "HELLO"


# ============================================================================
# B.  WRITE YOUR FIRST DECORATOR
# ============================================================================

# ----- Exercise 2 ------------------------------------------------------------
# Write a decorator `announce` that prints "CALLING..." before the function
# runs, and "DONE" after, without changing the function's return value.
def announce(func):
    # Your code:
    def wrapper(*args, **kwargs):
        print("CALLING...")
        result = func(*args, **kwargs)
        print("DONE!")
        return result
    return wrapper
        
       

@announce
def add(a, b):
    return a + b

# Test:
# print(add(2, 3))
# expected output:
#   CALLING...
#   DONE
#   5


# ----- Exercise 3 ------------------------------------------------------------
# Write a decorator `double_result` that DOUBLES whatever the wrapped
# function returns.
def double_result(func):
    # Your code:
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper
    

@double_result
def get_number():
    return 7

@double_result
def add(a, b):
    return a + b

# Test:
print(get_number())    # 14
print(add(2, 3))       # 10


# ============================================================================
# C.  THE TIMER 
# ============================================================================

# ----- Exercise 4 ------------------------------------------------------------
# Write a decorator `timer` that:
#   - records the time BEFORE the function runs
#   - records the time AFTER
#   - prints how long it took, like: "slow_func took 0.5012 seconds"
#   - returns the function's actual result unchanged
# Use time.time() for timing, and func.__name__ to get the function's name.
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper
@timer
def slow_square(n):
    time.sleep(0.2)
    return n * n

# Test:
result = slow_square(5)
print(result)
# expected:
#   slow_square took 0.2003 seconds
#   25


# ============================================================================
# D.  ONE PREDICTION EXERCISE
# ============================================================================

# ----- Exercise 5 ------------------------------------------------------------
# PREDICT what this prints. Don't run it yet.
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] calling {func.__name__} with {args}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned {result}")
        return result
    return wrapper

@logger
def multiply(a, b):
    return a * b

print(multiply(3, 4))
#
# My prediction (three lines, in order): 
# [LOG] calling multiply with a, b
# # [LOG] multiply return 12

