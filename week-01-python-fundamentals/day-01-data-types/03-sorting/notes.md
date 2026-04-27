Sorting: .sort() and sorted() and the key parameter


lst.sort() -> sorts in place, mutates, and returns None, works ony in list

sorted(lst) -> returns a new list, original list remains untouched, works on any iterable


When used sorted() always returns a list no matter what the input type was


Anything that can be comparible in one data type can be sorted


now key parameter

By default, Python sorts by comparing elements < between them. That works for nuber, strings, and tuples of comparible things.

For anything complex we use key

key is a fuction