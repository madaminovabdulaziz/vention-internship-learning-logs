"""
================================================================================
 DAY 1 · PART 3 — SORTING — EXERCISES
================================================================================
 7 exercises. ~30 minutes.
 Same rules: predict first, run, note what surprised you.
 Hints at the bottom.
================================================================================
"""
 
# ============================================================================
# A.  WARMUP — `.sort()` vs `sorted()`
# ============================================================================
 
# ----- Exercise 1 ------------------------------------------------------------
# Predict what each `print` produces.
a = [3, 1, 4, 1, 5, 9, 2, 6]
# print(sorted(a))
# print(a)                   # did sorted() mutate a? # No
# print(a.sort())            # what does .sort() return? list in sorted order
# print(a)                   # did .sort() mutate a? yes
# My predictions: 

# ----- Exercise 2 ------------------------------------------------------------
# Sort these words by LENGTH, ascending.
words = ["elephant", "cat", "hippopotamus", "ant", "dog", "butterfly"]
# Your code:
by_length = None
 
print(sorted(words, key=len))

 
# ----- Exercise 3 ------------------------------------------------------------
# Sort these strings case-insensitively.
names = ["alice", "Bob", "charlie", "Dave", "eve"]
# Your code:
case_insensitive = None
print(sorted(names, key=str.lower))


 
# ----- Exercise 4 ------------------------------------------------------------
# A list of student records. Sort them by GPA, highest first.
students = [
    {"name": "Alice",  "gpa": 3.7},
    {"name": "Bob",    "gpa": 3.9},
    {"name": "Carol",  "gpa": 3.5},
    {"name": "Dan",    "gpa": 3.9},
]
# Your code:
by_gpa = None
print(sorted(students, key=lambda s: s["gpa"], reverse=True))


# ============================================================================
# C.  MULTI-KEY SORTING
# ============================================================================
 
# ----- Exercise 5 ------------------------------------------------------------
# Sort `students` by GPA descending, AND for equal GPAs, by name ascending.
# (So Bob and Dan both have 3.9, but Bob should come first alphabetically.)
# Your code:
sorted_students = None
print(sorted(students, key=lambda s:(-s["gpa"], s["name"])))


 
# ============================================================================
# D.  REAL-WORLD PRACTICE
# ============================================================================
 
# ----- Exercise 6 ------------------------------------------------------------
# Given a list of (word, count) pairs, return the TOP 5 most frequent words.
# If counts are equal, sort alphabetically (ascending) to break ties.
pairs = [
    ("apple", 5), ("banana", 3), ("cherry", 5), ("date", 2),
    ("elder", 7), ("fig", 1),    ("grape", 5), ("honeydew", 7),
]
def top_5(pairs):
    # Your code:
    return sorted(pairs, key=lambda p: (-p[1], p[0]))[:5]
# Expected (by count desc, name asc):
# [('elder', 7), ('honeydew', 7), ('apple', 5), ('cherry', 5), ('grape', 5)]
 

 # ----- Exercise 7 ------------------------------------------------------------
# Sort a dict by VALUE (descending), returning a NEW dict.
# (Requires Python 3.7+, which preserves insertion order.)
scores = {"alice": 85, "bob": 92, "carol": 78, "dan": 92, "eve": 85}
# Your code:
sorted_scores = None
# Expected insertion order in the new dict:
# bob 92, dan 92, alice 85, eve 85, carol 78
# (ties broken by original insertion order since sort is stable)
print(dict(sorted(scores.items(), key=lambda kv: kv[1], reverse=True)))