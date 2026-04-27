Iterable -> something I can iterate over (a thing that has __iter__)

Iterator -> something that actually produces values one at a time has (__next__)


Lists, strings, dicts, sets, files all of the are iterables and implement __iter__() which returns an itertor




Key rules:

1. __iter__() returns iterator object, usually returns self


2. __next__() returns next value or raises StopIteration to signal no more values


3. A for loop keeps calling __next__() untit it sees StopIteration


RUle of thumb:

iterable = you can start iterating over me
iterator = I am currenntly being iterated, I know what's next