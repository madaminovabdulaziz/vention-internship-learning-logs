"""
================================================================================
 DAY 1 · PART 5 — COMPREHENSIONS & GENERATORS — EXERCISES
================================================================================
 9 exercises.
================================================================================
"""

# ============================================================================
# A.  WARMUP — write comprehensions from scratch
# ============================================================================

# ----- Exercise 1 ------------------------------------------------------------
# Use a LIST comprehension for each:
# (a) squares of numbers 1..10
# (b) only EVEN numbers from 1..20
# (c) uppercased versions of the words in this list
words = ["hello", "world", "python"]
squares = [x*x for x in range(1, 11)]          # (a)
evens   = [x for x in range(1, 21) if x % 2 == 0]          # (b)
upper   = [w.upper() for w in words]          # (c)


# ----- Exercise 2 ------------------------------------------------------------
# Use a SET comprehension:
# (a) all unique first letters in the given words
# (b) unique lengths among the given words
names = ["alice", "bob", "anna", "carl", "david", "dana"]
first_letters = {n[0] for n in names}    # (a)
unique_lengths = {len(n) for n in names}   # (b)


# ----- Exercise 3 ------------------------------------------------------------
# Use a DICT comprehension:
# (a) map each word to its length
# (b) invert this dict (swap keys and values)
sentence = ["apple", "banana", "cherry"]
lengths = {w: len(w) for w in sentence}                                     # (a)

d = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in d.items()}                                    # (b)


# ============================================================================
# B.  CONDITIONAL EXPRESSIONS vs FILTERS
# ============================================================================

# ----- Exercise 4 ------------------------------------------------------------
# Given numbers 1..10, build a list where:
#   - odd numbers are kept as-is
#   - even numbers are replaced with 0
# Result should be the SAME LENGTH as 1..10. (Hint: this is a branch, not a filter.)
# Your code:
result_4 = [n if n % 2 == 1 else 0 for n in range(1, 11)]
# Expected: [1, 0, 3, 0, 5, 0, 7, 0, 9, 0]


# ----- Exercise 5 ------------------------------------------------------------
# Given numbers 1..10, build a list containing ONLY the odd numbers squared.
# (Hint: this IS a filter.)
# Your code:
result_5 = [n*n for n in range(1, 11) if n % 2 == 1]
# Expected: [1, 9, 25, 49, 81]


# ============================================================================
# C.  GENERATOR EXPRESSIONS — the memory lesson
# ============================================================================

# ----- Exercise 6 ------------------------------------------------------------
# Run this block AS IS. Observe the size difference.
import sys

big_list = [x * x for x in range(1_000_000)]
big_gen  = (x * x for x in range(1_000_000))

print("list size:", sys.getsizeof(big_list), "bytes")
print("gen  size:", sys.getsizeof(big_gen),  "bytes")
# Takeaway note:
# list computes and stores all values now, gen stores the recipe and computes values on demand


# ----- Exercise 7 ------------------------------------------------------------
# Compute the sum of squares of numbers 1..100 in two ways. Both should give
# the same number, but one of them is more memory-efficient.
sum_via_list = sum([x * x for x in range(1, 101)])       # use a list comprehension
sum_via_gen  = sum(x*x for x in range(1, 101))       # use a generator expression inside sum()
# Which one is idiomatic and why?
# My note:



# ----- Exercise 8 ------------------------------------------------------------
# A generator is ONE-SHOT. Predict what these prints show:
gen = (x for x in range(3))
# print(list(gen)) 
# print(list(gen))
# My prediction: 

# print(list(gen))  -> [0, 1, 2]
# Second will be empty

# ============================================================================
# D.  REAL-WORLD PRACTICE
# ============================================================================

# ----- Exercise 9 ------------------------------------------------------------
# From the given records:
#   (a) get the set of unique cities using a set comprehension
#   (b) build a dict mapping each city to the LIST of user names there,
#       using a regular loop (hint: setdefault). Then explain why a single
#       comprehension is awkward here.
#   (c) using any comprehension you like, return the list of adult users
#       (age >= 18) — just their names, as a list.
users = [
    {"name": "Alice", "age": 30, "city": "NYC"},
    {"name": "Bob",   "age": 17, "city": "LA"},
    {"name": "Carol", "age": 22, "city": "NYC"},
    {"name": "Dan",   "age": 15, "city": "Chicago"},
    {"name": "Eve",   "age": 45, "city": "LA"},
]

unique_cities = {u['city'] for u in users}            # (a) — set comprehension
by_city = {}                    # (b) — regular loop
adult_names = [u['name'] for u in users if u['age'] >= 18]              # (c) — list comprehension

