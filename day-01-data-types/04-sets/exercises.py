"""
================================================================================
 DAY 1 · PART 4 — SETS — EXERCISES
================================================================================
 6 exercises. 

================================================================================
"""

# ============================================================================
# A.  ALGEBRA DRILLS
# ============================================================================

# ----- Exercise 1 ------------------------------------------------------------
# Two classes of students. Compute:
#   - students in BOTH classes
#   - students in ONLY the Python class
#   - students in ONLY the JS class
#   - students in EITHER (all unique)
#   - students in ONE class but not both
python_class = {"Alice", "Bob", "Carol", "Dan"}
js_class     = {"Bob", "Eve", "Carol", "Frank"}

both        = python_class | js_class
only_python = python_class - js_class
only_js     = js_class - python_class
either      = python_class & only_js
exclusive   = python_class.symmetric_difference(js_class)


# ============================================================================
# B.  DEDUPLICATION & MEMBERSHIP
# ============================================================================

# ----- Exercise 2 ------------------------------------------------------------
# Given a list of words (possibly with duplicates), return a list of UNIQUE
# words preserving their first-seen order. Do NOT use set() alone (it loses
# order). Use a set for fast membership checks + a list for order.
def unique_preserve_order(words):
    # Your code:
    seen = set()
    result = []
    for w in words:
           if w not in seen: seen.add(w); result.append(w)
    return result

# Test:
# print(unique_preserve_order(["apple","banana","apple","cherry","banana","date"]))
# expected: ['apple','banana','cherry','date']


# ----- Exercise 3 ------------------------------------------------------------
# Given a big list of user_ids and a "banned" list, return only the
# non-banned user_ids. Make it FAST even if the lists are large.
# (Hint: membership test in a list is O(n), in a set is O(1).)
def filter_banned(user_ids, banned):
    # Your code:
    banned = set()
    return [u for u in user_ids if u not in banned]

# Test:
# print(filter_banned([1,2,3,4,5,6], [2,4,6]))     # [1, 3, 5]


# ============================================================================
# C.  FROZENSET
# ============================================================================

# ----- Exercise 4 ------------------------------------------------------------
# You have pairs of people who collaborated. The pair (Alice, Bob) is the
# same as (Bob, Alice). Build a SET of unique collaborations from the
# following list. Each collaboration should be a frozenset so order doesn't
# matter.
raw_pairs = [
    ("Alice", "Bob"),
    ("Bob",   "Alice"),    # duplicate of above
    ("Carol", "Dan"),
    ("Alice", "Carol"),
    ("Dan",   "Carol"),    # duplicate of Carol-Dan
]
unique_collaborations = {frozenset(pair) for pair in raw_pairs}
# Expected: a set containing 3 frozensets:
# {frozenset({'Alice','Bob'}), frozenset({'Carol','Dan'}), frozenset({'Alice','Carol'})}


# ----- Exercise 5 ------------------------------------------------------------
# Use a frozenset as a DICT KEY. Build a dict that maps a set of ingredients
# to a recipe name. Then look up a recipe by passing the ingredients in a
# DIFFERENT order — it should still find the recipe.
recipes = {}
recipes[frozenset({"flour","egg","sugar"})] = "cake"
# Add these entries:
#   frozenset({"flour","egg","sugar"}) -> "cake"
#   frozenset({"flour","water","salt"}) -> "bread"
#   frozenset({"egg","cheese","bread"}) -> "grilled_cheese"

# Your code to populate recipes:


# Now look up a recipe by a set written in a different order:
# query = frozenset({"sugar", "egg", "flour"})      # reorder of cake ingredients
# print(recipes[query])      # should print "cake"


# ============================================================================
# D.  REAL-WORLD PRACTICE
# ============================================================================

# ----- Exercise 6 ------------------------------------------------------------
# Given a list of tag-lists for each article, find:
#   (a) the set of ALL unique tags that appear anywhere
#   (b) the set of tags that appear in EVERY article (intersection across all)
# Use set algebra, not manual loops inside loops.
articles = [
    ["python", "beginner", "tutorial"],
    ["python", "advanced", "tutorial"],
    ["python", "tutorial", "testing"],
]
def all_tags(articles):
    result = set()
    for a in articles: result |= set(a)
    return result


def common_tags(articles):
    # Your code (hint: intersect starting from the first article's set)
    result = set(articles[0])
    for a in articles[1:]: result &= set(a)
    return result
# Tests:
# print(all_tags(articles))     # {'python','beginner','tutorial','advanced','testing'}
# print(common_tags(articles))  # {'python','tutorial'}

