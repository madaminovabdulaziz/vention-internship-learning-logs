Use classes when I have a thing with it's own:
1. State
2. Operations that make sense on it
3. Rules about valid states



The rule for my brain

instance.x = value creates/updates an attribute on the instance. Never on the class.
Class.x = value creates/updates an attribute on the class. Affects all instances (except those that have their own shadow).

If you want to change shared state: touch the class.
If you want to change instance state: touch the instance.



Rule: use classes when you have a state that persists and operations that work on that state. 

Use a function when you have input -> output


Why we use self?

This is just a convention, Python does not care, we can write foo for example, but we should not.

__init__ is a dunder method, Dunder is for Double Underscore, dunders are methods Python calls automatically at specific moments

__init__ -> called when instantiate Dog(...)
__repr__ -> calked when I call print() or repr() the object
__eq__ -> called when you see ==

__len__-> called when we use len()
__add__ -> calledn when we use +


Now, let's talka about instance attributes

```
class Dog:
    def __init__(self, name):
        self.name = name # -> instance attribute


rex = Dog("REX")

print(rex.name)

```

each instance has it's own copy. Changing rex.name does not affect buddy.name



Now let's talk about "Class attributes"

Class attributes are defined outside counstruction __init__, I mean, if we write attribute inside __init__ it means we are doing instance attribute right, but class attribuets are different.

They defined inside a class, before __init__ constructor, which means, they are shared, like a global variable belongs to that class. It is defined outside of any method

```

class Dog:
    species = "German Shepherd"
    legs = 4

    def __init__(self, name):
        self.name = name
    


rex = Dog("Rex")
buddy = Dog("Buddy")


print(rex.species)    # Canis familiaris
print(buddy.species)  # Canis familiaris
print(Dog.species)    # Canis familiaris — access via class too

```
So when we write rex.species, python looks in 2 places:

1. First, instance's own dictionary: rex.__dict__ -> does rex have its own species? No
2. Then the classe's dictionary: (Dog.__dict__) -> does Dog have species? Yes, return it

When you write rex.name:

Instance dict — yes, rex has its own name (set in __init__). Return it. Stop.


THE RULE:
If attribute is mutable like (list, dict, set, object) and it belongs to each instance -> put in __init__

If it's immutable (string, number, tuple, bool) and shared across all instances -> class attribute is fine


Another important thing to keep in mind is that:
when we doing class attributes, and we assigned "another" value to initial class attribute, it does not modify the original value of class attribute, instead, each object gets it's own value, it creates a new instance attribute that shadows 




But mutation is different, if we using  mutable attribute like list, dict etc, them i that case, it wil chage 