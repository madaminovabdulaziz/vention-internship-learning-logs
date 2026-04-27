class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius


    # INSTANCE Method -- needs t self.celsius
    def to_fahrenheit(self):
        return self.celsius * 9/5 + 32
    
    @classmethod 
    def from_fahrenheit(cls, f):
        celcius = (f - 32) * 5/9
        return cls(celcius)

    @staticmethod
    def is_freezing(celsius):
        return celsius <= 0
    




class Demo:
    # without the decorator
    @staticmethod
    def with_self(x):              # only one parameter, no self
        print("got:", x)

d = Demo()
d.with_self(5)
# TypeError: with_self() takes 1 positional argument but 2 were given
# (Python tried to pass d AND 5 — that's 2 arguments, but you only declared 1)




class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"
    

p = Point(3, 4)

print(p)
repr(p)


# RULE OF THUMB: Every class I write should have a __repr__. It costs 30 seconds, and saves hours of 


