The property setup has three required pieces


```

class Thing:
    def __init__(self, value):
        self._x = value # (1) storage - conventionally prefixed with _

    @property
    def x(self):
        return self._x  # (2) getter - has SAME NAME as the public API

    
    @x.setter # (3) setter -- decorator is @<getter_name>.setter
    def x(self, value): # same name, takes (self, value)
        self._x = value

```

2 facts worth knowing

1. The storage attribute "_x" is different from the property name "x", if I store it as self.x, will be infinite recursion

2. The getter and setter functions (methods) should have same name, 


I have learned that @propert helps value sync automatically

ex:
```
r = Rectangle(3, 4) 
print(r.area) # 12

r.width = 10

print(r.area) # Still 12

```


with @property it is always current


The real test — why not just use a method?
This is the fair question your gut is asking. Python already has methods. Why add @property at all if the only gain is removing parens?
Here's the honest answer: convention signals intent.

r.area() says to a reader: "this is an action you perform. It might be expensive, it might have side effects, it might return something different each time."
r.area says to a reader: "this is a value. It's part of what a rectangle fundamentally is. Cheap, no side effects, conceptually just data."




IMPORTANT: When I should reach for a property

1. Is it just a stored with no rules? -> public attribute (self.x)
2. Does it need vaidation, type checking, or logging on read/write? -> property with getter/setter
3. Is it computed from other attributes? -> read-only property (getter only)
4. Is it expensive to compute and should be cached? -> property



The property is the public face. The underscore-prefixed attribute is the storage. They must have different names, or the property will infinitely recurse into itself. All code — inside or outside the class — talks to the property name. Only the getter and setter touch the underscore name directly.