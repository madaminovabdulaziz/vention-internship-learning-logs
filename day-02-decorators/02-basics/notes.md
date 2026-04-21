Decorator basics


CORE IDEA:

A decorator is a function that:

1. Takes a function as input
2. Returns a new function that wraps the original -- usually adding something before, after, or around it.

So the whole idea of decorators is that, eventhough Python "functios" solve "code repetition" - problem,
decorator solves repitited behavior of functions. That is, decorator says: Let me add behavior to functions without modifying the functions themselves. Period.


Example, let's assume we should calculate and return  how long each funtinon takes to run.

```
import time

def add(a, b):
    start = time.time()
    result = a + b
    end = time.time()
    print(f"add took {end - start} seconds")
    return result

def subtract(a, b):
    start = time.time()
    result = a - b
    end = time.time()
    print(f"subtract took {end - start} seconds")
    return result

# ... same for multiply, and 50 other functions

```

What if we could write timing logic once, and apply it to any function we want?


```
@timer
def add(a, b):
    return a + b

@timer
def subtract(a, b):
    return a - b

```


Now, above examples were for functions that do not take any argument right, now how to make functions, I mean specifically wrapper to accept any arguments?

THE ANSWER: use *args, **kwargs

```
def shout(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


@shout
def greet(name):
    return f"Hello, {name}"


@shout
def announce(prefix, message):
    return f"{prefix}: {message}"



print(greet("Alice"))
print(greet("Warning", "too hot"))
