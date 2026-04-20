Day 1, Part 1, Muttable / Immutale data types

So first off all I must admit, that everything in Python language is an object. And every object has 3 things.

1. Identity -> Where it lives in memory -> call by command: id(obj)
2. Type -> What kind of object it is -> call by command: type(obj)
3. Value -> What data it holds -> obj itself


So what is the difference between mutable and immutable data types?

Well, mutable data types are usually can be changes in place, with the trick, same "id", but contents might be different

On the other hand, immutable data type's value is frozen, if we want to do changes, we need to create a new object


Common examples for both data types:
Mutable: list, dict, set
Immutable: string, int, float, bool, tuple, frozenset, NoneType



Immutable types:

bool -> is subclas of int, True means 1, False means 0

I have learned that as Python caches ints from -5 t0 256, NEVER USE is for numeric comparison, USE ==

---------------

str -> Strings are immutable, hashable, iterable, sliceable

So, when we try to change str, like making it uppercase or sort etc, new object with different ID always is opened, 
because as I learned strings are immutable. Every mutations produces a new string

----------------

Now let's talk about tuples and their hashability

What I have learned is that, tuples are hashable only if every element inside a tuple is hashable
Ex: (1, 2, 3, (4, 5)) -> Hashable
(1, 2, [3]) -> Not hashable


Also, as tuple's can't be changed, we can say smth like: this has a fixed shape, do not append to it. It is not a collection (list, dict), it is a RECORD.

Another IMPORTANT fact about tuple is that, simple (1) does not mean that this is tuple, coz (1) is simple parentheses
which can be used in math formulas, like (2+5)
SO
what makes it tuple is: (1,) -> called trailling comma


----------------

frozenset -> frozenset is "fixed" or let's say "frozen" type of set. Remember, that set is mutable, but frozenset is immutable.

frozenset is kinda inherited all types or behaviour from set. It means, it is unordered, only unique elements, also hashable as dictionaries. 

So difference between dict and set/frozenset is that dict has key-value pairs while set has only values.

IMPORTANT about frozenset: you can't do any operation like: .add, .remove, .discard, .pop, .clear on frozenset.

When to use it? So we should basically use it when "set" needs to be a dict key, coz set can't be hashed, as dict keys should be hashed, set is mutable -> meaning not hashable -> can't be a key




-------------------------------------------------------------------



Mutable types


list -> ordered, indexed, iterable, allows duplicates, grows/shrinks

Ok, what I have learned that methods that mutate/change in place return None,  Python build-in functions return new object

In place methods that return None:
lst.sort()
lst.reverse()
lst. append(x)
lst.extend(int)
lst.clear()


Returns new object:
sorted(list)
reversed(list)
lst + [x]
lst + list(int)
[]


[x] * n creates n references to the same x. Safe if x is immutable (int, str, tuple). A trap if x is mutable (list, dict, set). For mutable elements, always use [new_x() for _ in range(n)] instead.

---------------


dict -> is dictionary, always with key and values. Key is always should be hashable, values does not matter

core methods:
d.keys() -> returns keys
d.values() -> returns values
d.items() -> can be iterated with loop to get both keys and values


d.get(key, default) -> get value with key, if no key in dict, return with default one
d.pop(key, default) -> removes and returns, raises KeyError without default
d.setdefault(key, default) -> if key is missing, inserts default value and returns it
d.update(info) -> mergers info into d in place



---------------


set -> unordered collections of unique, hashable elements (values) -> means same like dict but without keys

Remember that {} is empty dict, not an empty set eventhough, to declare a set we are opening same brackets like
my_Set = {} -> but this is dict
my_Set = set() -> is now set 

for empty sets of course

Methods & Operations in sets:

Union: a | b or a.union(b) -> returnes elements in 2 sets
Intersection: a & b or a.intersection(b) -> returns intersection from given 2 sets
Difference: a - b or a.difference(b) -> returns differnce betwene 2 sets

