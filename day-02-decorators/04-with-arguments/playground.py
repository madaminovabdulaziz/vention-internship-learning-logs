from functools import wraps

def repeat(n):                     # "the factory"
    def inner_decorator(func):     # "the real decorator"
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return inner_decorator



@repeat(3)
def say_hi(name):
    print(f"Hi, {name}!")
    return name

say_hi('Alice')