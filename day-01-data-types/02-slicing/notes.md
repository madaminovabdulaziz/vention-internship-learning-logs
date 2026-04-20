Slicing is a way to cut a data type

Slicing works in any ordered, indexable sequence: str, list, tuple, bytes, range

It does not work pn set, frozenset, dict, coz they are nor ordered/indexable that way.


IMPORTANT: slicing always returns new object, it never changes the original data type values, it's always a read
operation that produces a copy

that says:
str slice -> new str
list slice -> new list
tuple slice -> new tuple


Slicing has 3 parts:
start
stop
step

like in for loops


all three are optional

There is one rule in slicing: stop is exclusive
I mean, when you define at which index to stop slicing, that index will not be taken, it will be exclusive


Some defaults:

a[:] - > whole sequence (shallow copy)
a[2:] from index 2 to the end
a[:5] from index 0 till index 5, but index 5 will not be taken
a[::2] every other element
a[::-1] reversed string

s = "hello"
print(s[-1])        # "o"      (last char)
print(s[-2])        # "l"
print(s[-3:])       # "llo"    (last 3 chars)
print(s[:-2])       # "hel"    (everything except last 2)


negative step means going backwords


Slice Objects 
s = slice(1, 5, 2)
another way to slice a string

