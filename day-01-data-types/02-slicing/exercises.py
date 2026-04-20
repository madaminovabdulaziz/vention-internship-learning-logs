"""
================================================================================
 DAY 1 · PART 2 — SLICING — EXERCISES
================================================================================
Same rules:
1. PREDICT the output in a comment before running.
2. Run and compare.
3. If wrong, write a 2-line note on why.
4. Hints at the bottom — don't peek early.
 
 8 exercises.
================================================================================
"""
 
# ============================================================================
# A.  WARMUP — predict the output (slices on a string)
# ============================================================================
 
s = "PYTHONISTA"
 
# ----- Exercise 1 ------------------------------------------------------------
# Predict each. Then run them all.
# a = s[0:3] -> PYT
# b = s[3:] -> HONISTA
# c = s[:4] -> PYTH
# d = s[-3:] -> 
# e = s[:-3] -> PYTHONI
# f = s[1:-1] -> YTHONIST
# My predictions: 

print(s[0:3])
print(s[3:])
print(s[:4])
print(s[-3:])
print(s[:-3])
print(s[1:-1])



# ----- Exercise 2 ------------------------------------------------------------
# Predict:
# a = s[::2] PTOIT
# b = s[1::2] YHNSA
# c = s[::-1] ATSINOHTYP
# d = s[::-2] ASNHY
# e = s[5:1:-1] HONT
# My predictions:
 
 

# ----- Exercise 3 ------------------------------------------------------------
# Out-of-bounds behavior. Predict:
# a = s[100:200] " "
# b = s[-999:3] PYT
# c = s[0:9999] "PYTHONISTA"
# d = s[5:2]     INDEXERROR    # start > stop with positive step — what happens?
# My predictions:



# ============================================================================
# B.  SMALL TASKS — write the slice
# ============================================================================
 
# ----- Exercise 4 ------------------------------------------------------------
# Given a list, return:
#   - the first 3 elements
#   - the last 3 elements
#   - everything except first and last
#   - the list reversed
# Use slicing for all four. One line each.
nums = [10, 20, 30, 40, 50, 60, 70]
first_three = None      # [:3]
last_three  = None      # [-3:]
middle      = None      # [1:-1]
reversed_   = None      # [::-1]
 


def is_palindrome(s):
    # Your code (1 line body):
    
    return s == s[::-1]
# Tests:
# print(is_palindrome("racecar"))   # True
# print(is_palindrome("hello"))     # False
# print(is_palindrome(""))          # True (empty is trivially palindrome)
 


 # ----- Exercise 6 ------------------------------------------------------------
# Given a list, split it into two halves and return them as a tuple
# (first_half, second_half). If the length is odd, put the middle
# element in the first half.
def halve(lst):
    # Your code:
    return (lst[:len(lst)//2], lst[len(lst)//2:])
# Tests:
# print(halve([1,2,3,4]))       # ([1,2], [3,4])
# print(halve([1,2,3,4,5]))     # ([1,2,3], [4,5])
# print(halve([]))              # ([], [])
 


# ============================================================================
# C.  MUTATION — slice assignment (lists only)
# ============================================================================
 
# ----- Exercise 7 ------------------------------------------------------------
# PREDICT each one separately. Reset lst each time.
# Case 1:
# lst = [1, 2, 3, 4, 5]
# lst[1:3] = [20, 30, 40]
# print(lst) [1, 20, 30, 40, 4, 5]
#
# Case 2:
# lst = [1, 2, 3, 4, 5]
# lst[:] = [99, 100] 
# print(lst) [99, 100]
#
# Case 3:
# lst = [1, 2, 3, 4, 5]
# lst[::2] = [0, 0, 0]        # assign with a step — tricky!
# print(lst) 
#
# Case 4:
# lst = [1, 2, 3, 4, 5]
# lst[::2] = [0, 0]           # mismatch in length — what happens?
# print(lst)
# My predictions:
 
 