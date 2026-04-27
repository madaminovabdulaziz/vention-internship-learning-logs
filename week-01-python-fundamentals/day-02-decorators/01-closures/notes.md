Closures


A closure is the function inside a function that remembers variables outside the inner function.

When Python sees a name inside a function, it looks up in this order:

L -> E -> G -> B

L -> Local -> is it defined in this inner function?

E -> Enclosinng -> is it defined in enclosing (outer) function?

G -> Global -> is it defined in module level? I mean in this python file?

B -> Built-in -> is it builr in? Like: print, len etc



```
x = "global"

def outer():
    x = "enclosing" 
    def inner():
        x = "local"
        print(x)
    inner() # prints "local" -> Found at L

outer()

```


Reading vs. Writing


```
def outer():
    counter = 0
    def inner():
        counter += 1 # ERRRORR
        print(counter)
    inner()


```


The moment Python sees couner+=1 -> it searches from local varibles, and of courses it could not find it. 
Python does not mix "local" and "enclosing" for the same name, the assignment makes the whole function treat as count as local, and now the read at the same line fails


The Fix

add nonlocal


We don't need nonlocal when mutating
ex:

```
items = []
def add(x):
    items.append(x)
```


We DO need to use nonlocal when rebinding:

```
items = []
def add(x):
    nonlocal items
    items = items + [x]

```


NOTE: Python only triggers "oh this is local" only when it sees "=", method calls like .append() ignored!



What I have learned:
nonlocal exists for ONE reason: letting inner functions reassign variables in outer scope

mutation != rebinding