"""
================================================================================
 DAY 1 · PART 6 — DICTIONARIES — EXERCISES
================================================================================
 7 exercises. 
================================================================================
"""

# ============================================================================
# A.  METHODS — predict the behavior
# ============================================================================

# ----- Exercise 1 ------------------------------------------------------------
# Predict each print. Reset d between groups if a line mutates it.
d = {"a": 1, "b": 2, "c": 3}

# print(d.get("a"))            # 1
# print(d.get("z"))            # None
# print(d.get("z", -1))        # -1
# print(d["z"])                # Key Error

# d.pop("a")                   # 1
# print(d)                     # None
# d.pop("x", "missing")        # missing

# My predictions:



# ----- Exercise 2 ------------------------------------------------------------
# What's the difference between these three, and which one ends up with
# independent lists per key?
a = dict.fromkeys(["x", "y", "z"], [])
b = {k: [] for k in ["x", "y", "z"]}
c = dict.fromkeys(["x", "y", "z"], list())    # is list() called once or 3 times?

a["x"].append(1)
b["x"].append(1)
c["x"].append(1)
# print(a, b, c)
# My predictions and explanation: ___________________________________________


# ============================================================================
# B.  ITERATION
# ============================================================================

# ----- Exercise 3 ------------------------------------------------------------
# Given this dict, print its contents in three different orders:
#   (a) natural (insertion) order
#   (b) alphabetical by key
#   (c) by value, descending
scores = {"alice": 85, "bob": 92, "carol": 78, "dan": 90}

# (a)
for k, v in scores.items(): print(k, v)

# (b)
for k, v in sorted(scores.items()): print(k, v)

# (c)
for k, v in sorted(scores.items(), key=lambda kv: kv[1], reverse=True):
    print(k, v)


# ----- Exercise 4 ------------------------------------------------------------
# Remove all entries from this dict where the value is less than 50.
# Write TWO versions:
#   (a) mutate the original dict (use list(d) for snapshot)
#   (b) build a new filtered dict (comprehension)
inventory = {"apples": 120, "bananas": 30, "cherries": 45, "dates": 200, "eggs": 12}

# (a) in-place:
for k in list(inventory):
    if inventory[k] < 50:
        del inventory[k]

# (b) new dict:
filtered = {k: v for k, v in inventory.items() if v >= 50}


# ============================================================================
# C.  REAL-WORLD PATTERNS
# ============================================================================

# ----- Exercise 5 ------------------------------------------------------------
# Group these words by their length. Use setdefault, no defaultdict.
words = ["hi", "hey", "hello", "world", "no", "yes", "python", "code", "go"]
by_length = {}
# Your code:
for w in words:
    by_length.setdefault(len(w), []).append(w)
# Expected: {2: ['hi','no','go'], 3: ['hey','yes'], 5: ['hello','world'],
#            6: ['python'], 4: ['code']}   (order may vary inside lists)


# ----- Exercise 6 ------------------------------------------------------------
# Merge these two dicts — later values should overwrite earlier ones.
# Show THREE ways to do it (any Python 3.7+ versions).
defaults = {"theme": "light", "font": "sans", "lang": "en"}
user     = {"theme": "dark", "lang": "ru"}

way1 = {**defaults, **user}   # using {**...}
way2 = defaults | user   # using | (3.9+)
way3 = defaults.copy(); way3.update(user)   # using .update() on a copy
# Expected (all three equal):
# {'theme': 'dark', 'font': 'sans', 'lang': 'ru'}


# ============================================================================
# D.  TIES INTO EARLIER TOPICS
# ============================================================================

# ----- Exercise 7 ------------------------------------------------------------
# A classroom dict mapping student_id -> {name, grades: [list of ints]}.
# Write a function `class_summary(classroom)` that returns a new dict:
#   student_id -> average grade (float)
# Requirements:
#   - Use a dict comprehension
#   - If a student has no grades, their average is 0
classroom = {
    101: {"name": "Alice", "grades": [85, 92, 78]},
    102: {"name": "Bob",   "grades": [75, 80]},
    103: {"name": "Carol", "grades": []},
    104: {"name": "Dan",   "grades": [100, 95, 92, 98]},
}

def class_summary(classroom):
    # Your code:
   return {
        sid: (sum(info["grades"]) / len(info["grades"]) if info["grades"] else 0)
        for sid, info in classroom.items()
    }
# Expected:
# {101: 85.0, 102: 77.5, 103: 0, 104: 96.25}

