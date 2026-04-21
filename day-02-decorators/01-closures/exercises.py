"""
================================================================================
 DAY 2 · PART 1 — CLOSURES — EXERCISES
================================================================================
 7 exercises. ~30 minutes.
 Closures feel abstract the first time. Writing a few makes them concrete.

 Same rules: predict first, run, write a 2-line note on anything surprising.
================================================================================

"""

# ============================================================================
# A.  WARMUP — predict the output
# ============================================================================

# ----- Exercise 1 ------------------------------------------------------------
# Predict what each line prints.
def outer():
    x = 10
    def inner():
        return x
    return inner

f = outer()
print(f()) 
print(f())
print(f.__closure__)       # will print something — what is it roughly?
# My predictions:
# print(f())  -> 10
# print(f.__closure__)    -> cell at object XXXX


# ----- Exercise 2 ------------------------------------------------------------
# Predict — does this crash or run?
def outer():
    count = 0
    def inner():
        count = count + 1
        return count
    return inner

# f = outer()
# print(f())
# My prediction: it will crash! Because we did not use nonlocal keyword! When inner fucntions sees count it will
# seek from inner function


# ============================================================================
# B.  BUILD YOUR OWN
# ============================================================================

# ----- Exercise 3 ------------------------------------------------------------
# Write a function `make_counter()` that returns a new function. Each time
# you call that returned function, it returns the next number starting from 1.
# Two separate counters from two separate calls must be independent.
def make_counter():
    # Your code:
    count = 0
    def increment():
        nonlocal count
        count+=1
        return count
        
    return increment

# Test:
c1 = make_counter()
c2 = make_counter()
print(c1())   # 1
print(c1())   # 2
print(c1())   # 3
print(c2())   # 1  (independent)
print(c1())   # 4


# ----- Exercise 4 ------------------------------------------------------------
# Write a function `make_multiplier(n)` that returns a function which
# multiplies its argument by n.
def make_multiplier(n):
    # Your code:
    def multiplier(x):
        return x * n

    return multiplier

# Test:
double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))   # 10
print(triple(5))   # 15
print(double(10))  # 20


# ----- Exercise 5 ------------------------------------------------------------
# Write a function `make_averager()` that returns a function. The returned
# function accepts a number and returns the running average of all numbers
# given to it so far.
#
# You'll need to remember BOTH: the total and the count. Use nonlocal.
def make_averager():
    # Your code:
    # avrs = list()
    # count = 0
    # def append(x):
    #     nonlocal count
    #     if count == 0:
    #         avrs.append(x)
    #     avrs.append(sum(avrs) / count)
    #     count +=1 
    # return append

    # NOTE This code was full of bugs and now I am investigating why


    total = 0
    count = 0

    def append(x):
        nonlocal total
        nonlocal count
        total += x
        count += 1
        return total / count
    return append


        

# Test:
avg = make_averager()
print(avg(10))    # 10.0   (avg of [10])
print(avg(20))    # 15.0   (avg of [10, 20])
print(avg(30))    # 20.0   (avg of [10, 20, 30])



# NOTE (some)
# So now I understand why I did mistake and all these uneccessary complex things









# ============================================================================
# C.  THE LOOP TRAP
# ============================================================================

# ----- Exercise 6 ------------------------------------------------------------
# PREDICT the output. Think carefully before running.
funcs = []
for i in range(3):
    def f():
        return i
    funcs.append(f)

# print(funcs[0]())
# print(funcs[1]())
# print(funcs[2]())
# My prediction: 2




#
# Now FIX it so the output is 0, 1, 2. Use a default argument:
funcs_fixed = []
# Your code (build funcs_fixed using the default-arg trick):
for i in range(3):
    def f(i=i):
        return i
    funcs_fixed.append(f)



# ============================================================================
# D.  ONE SMALL CHALLENGE
# ============================================================================

# ----- Exercise 7 ------------------------------------------------------------
# Write `make_accumulator(start=0)` that returns a function. Each call to the
# returned function adds its argument to an internal total and returns the
# new total. Also expose a way to RESET the total back to the start.
#
# Hint: one approach is to return TWO functions from make_accumulator — one
# for adding, one for resetting. You return them as a tuple.
def make_accumulator(start=0):
    # Your code:
    total = start
    def add(x):
        nonlocal total
        total += x
        return total
    
    def reset():
        nonlocal total
        total = start
    return add, reset


# Test:
add, reset = make_accumulator(10)
print(add(5))    # 15
print(add(3))    # 18
print(add(2))    # 20
reset()
print(add(1))    # 11   (back to start=10, plus 1)

