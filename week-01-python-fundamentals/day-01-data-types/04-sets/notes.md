Sets

A set is unordered collection of unique, hashable elemets

Unordered means no index, no slice, no first element, we can iterate, but the order is insertion dependent


Unique means, duplicate elements dropped


Hashable elements only means we can't put a dict or a list in a set, we can put tuples if their values are hashable or frozensets


While set is mutable, frozenset is immutable

Set is not hashable, and can't be a dict key, whereas frozenst is hashable, can be a dict key, and can be element of another set


Adding to set is by method:
s = {1, 2, 4}

s.add(1)

Removing

s.remove(4)
if we do s.remove(111) -> where 111 does not exists in set, it will throw us an error.

So to avoid that we use s.discard(99)

s.pop() -> removes and returns an arbitrary element


s.clear() - empties the set



So set has a set algebra, where we can define union, intersection, difference, symmetric difference

So union -> A | B or A.union(B)
Ex: {1, 2, 3} | {3, 4, 5} -> {1, 2, 3, 4, 5}

Intersection -> A & B or A.intersection(B)
Ex: {1, 2, 3} & {2, 3, 4} # {2, 3}

Difference A - B or A.difference(B)
Means: Elements in A, but not in B

EX: {1, 2, 3} - {2, 3, 4} = {1}
{2, 3, 4} - {1, 2, 3} = {4} -> NOT symmetric



HASHABILITY of SETS

Elements must be hashable to be set to be hashable

{1, 2, (3, 4)}           # OK — tuple of hashables is hashable
{1, 2, [3, 4]}           # TypeError: unhashable type: 'list'
{1, 2, {3, 4}}           # TypeError: unhashable type: 'set'
{1, 2, frozenset({3,4})} # OK — frozenset is hashable



WHEN TO USE SET instead of LIST?


A. Is X in collection? 
SET time complexity - > O(1) -> Constant, very fast, instant lookup
LIST time complexity -> O(n) -> Slower




B. When we need remove duplicates -> use set

C. Set algebra in two collections



