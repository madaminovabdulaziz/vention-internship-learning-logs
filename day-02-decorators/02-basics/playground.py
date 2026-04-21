# A decorator without @ ( honest version )

def shout(func):
    def wrapper():
        ressult = func()
        return ressult.upper()
    return wrapper




def greet():
    return "Hello world!"

greet = shout(greet)

print(greet())


# Now let's do with decorator, actual @


@shout
def greet():
    return "Hello, world!"

print(greet())


# Now let's build a real timer with decorators, so it calculates function runtime


import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds!")
        return result
    
    return wrapper



@timer
def slow_add(a, b):
    time.sleep(0.5)
    return a + b



print(slow_add(9999, 1))