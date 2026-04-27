# ----- Exercise 1 ------------------------------------------------------------
# What prints?  Why?
a = [1, 2, 3]
b = a
b.append(4)
print(a)
# My prediction: a = [1, 2, 3, 4] Why? Because, b takes a variable's adress, reference and it updates a accordingly


# ----- Exercise 2 ------------------------------------------------------------
# What prints?  Why?
x = "hello"
y = x
y = y + " world"
# print(x)
# My prediction: hello world, the reason is the with above (Exercise 1)
# Actually I was wrong, the output was "hello", let me investigate it
# Now I understand, as strings are immutable, every change or mutation creates a new string object, therefore, 
# y became completely new object and any changes in y does not affect x


# ----- Exercise 3 ------------------------------------------------------------
# What prints?  Why?
t = (1, 2, 3)
#t[0] = 99
# My prediction: Error, tuples are immutable, once created they can't be changed


# ----- Exercise 4 ------------------------------------------------------------
# What prints?  Why?
s1 = {1, 2, 3}
s2 = {3, 2, 1}
print(s1 == s2)
print(s1 is s2)
# My prediction: first print will be True, because in set order of values does not matter,
# as for second print, it will return False, because s1 and s2 are different objects



# ----- Exercise 5 ------------------------------------------------------------
# What prints?  Why?  (Two separate questions.)
a = 256;  b = 256
c = 1000; d = 1001
print(a is b)
print(c is d)
# My prediction: First print is True, because, CPython will count them as equal from - 5 to 256, next one is False, as 
# c and d are different objects
# Actually, second print (c is d) is also True, let me investigate it
# Now I understand it, if two objects c and d in our case, point to the same object, in our case 1000, will return True


# ============================================================================
# B.  LEVEL 1 — basics
# ============================================================================
 
# ----- Exercise 6 ------------------------------------------------------------
# Given a list, return a NEW list with duplicates removed, preserving order.
# (Do not use dict.fromkeys yet — do it manually with a set for membership.)
def unique_preserving_order(items):
    # Your code:
    result = list()
    duplicate_remover = set()
    for item in items:
        duplicate_remover.add(item)
    
    for value in duplicate_remover:
        result.append(value)
    
    return result



 
# ----- Exercise 7 ------------------------------------------------------------
# Given two lists, return a tuple (common, only_in_a, only_in_b) using sets.
def compare(a: list, b:list):
    # Your code:
    common = set()
    only_in_a = set()
    only_in_b = set()

    for i in a:
        if i in b:
            common.add(x)
        else:
            only_in_a.add(x)
    
    for j in b:
        if y not in a:
            only_in_b.add(y)

    return (common, only_in_a, only_in_b)
            
    
# Test:
print(compare([1,2,3,4], [3,4,5,6]))  # expected: ({3,4}, {1,2}, {5,6})
 


# ----- Exercise 8 ------------------------------------------------------------
# Without using collections.Counter, count frequencies of characters in a
# string and return a dict. Then print the top 3 most frequent.
def char_frequencies(s):
    # Your code:
    my_dict = {}

    for c in s:
        my_dict[c] = my_dict.get(c, 0) + 1
    
    top_3 = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)[:3]
    print("Top most frequent:")
    for char, count in top_3:
        print(f" {char}: {count}")
    
    return my_dict




# ----- Exercise 9 ------------------------------------------------------------
# Make an immutable "point" you can use as a dict key. (Hint: tuple.)
# Then build a dict that maps each point to its distance from origin.
points = [(1, 2), (3, 4), (0, 5), (-1, -1)]
distances = {}
for p in points:
    x, y = p
    distances[p] = (x**2 + y**2) ** 0.5
print(distances)
# Your code:


 
# ----- Exercise 10 -----------------------------------------------------------
# Explain in a comment: why does .sort() return None but sorted() return a list?
# My answer: .sort() returns None, because it is immutable, but sorted() creates a new object



# ============================================================================
# C.  LEVEL 2 — the famous traps
# ============================================================================
 
# ----- Exercise 11 -----------------------------------------------------------
# The mutable default argument trap.
# Call `bag` three times with different values of x. What do you get?
def bag(x, container=[]):
    container.append(x)
    return container
 
print(bag("a"))
print(bag("b"))
print(bag("c"))
# My prediction: first print will return [a], next one [b], next one [c]
# Actually I was wrong, the result was surprising for me, as each time list has grown like:
# [a, b, c] Why? Let me investigate it
# Ok, now I understand it, when we giving a default, in our case is emopty list, it defines once, and it references to same 
# object I mean ID everytime

#
# Now rewrite it correctly below as `bag_fixed`:
def bag_fixed(x, container=None):
    # Your code:
    if container is None:
        container = []
    container.append(x)
    return container
 


 
# ----- Exercise 12 -----------------------------------------------------------
# The [[]] * 3 trap.
grid = [[]] * 3
grid[0].append("X")
# print(grid)
# My prediction: it will be [[X], [X], [X]]
#
# Now build `grid2` so that appending to grid2[0] does NOT affect the others.
# Your code:
grid2 = [[] for _ in (1, 2, 3)]


 
# ----- Exercise 13 -----------------------------------------------------------
# Shallow vs deep copy.
import copy
matrix = [[1, 2], [3, 4]]
m_shallow = matrix.copy()
m_deep    = copy.deepcopy(matrix)
m_shallow[0].append(99)
# print(matrix)
# print(m_shallow)
# print(m_deep)
# My prediction for each:
# print(matxrix) -> [[1, 2], [3, 4]]
# print(m_shallow) -> [[1, 2, 9], [3, 4]]

 