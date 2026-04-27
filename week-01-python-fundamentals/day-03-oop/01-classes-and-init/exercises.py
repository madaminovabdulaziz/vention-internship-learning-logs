"""
Day 3 · Part 1 — Exercises: Classes, __init__, and Attributes

HOW TO USE THIS FILE:
1. Work in order. Each exercise builds on the previous ones.
2. For "PREDICT" exercises, write your prediction as a comment BEFORE running.
   Then run, compare, and write a 1-line explanation if you were wrong.
3. Every exercise should be a working, runnable block. Test it.
4. When done, commit with:
   git add day-03-oop/01-classes-and-init/
   git commit -m "day-03 part 1: classes, init, attributes"

DIFFICULTY LEGEND:
  🟢 = Warm-up (syntax drill)
  🟡 = Applied (use the concept for something useful)
  🔴 = Trap (predict before running — the whole point is catching the gotcha)
  🟣 = Real-world (looks like code you'd write at work)
"""

# =============================================================================
# EXERCISE 1 🟢 — Your first class
# =============================================================================
# Define a class called `Book` with an __init__ that takes `title` and `author`.
# Create two Book instances and print each one's title and author.
#
# Expected output (example):
#   The Hobbit by Tolkien
#   1984 by Orwell


class Book:
    def __init__(self, title, author, year):
        self.title = title # NOTE: this is instance attributes
        self.author = author # NOTE: this is instance attributes
        self.year = year
        


    def describe(self):
        return f"'{self.title}' by {self.author} (published {self.year})"
    


book1 = Book("The Hobbit", "Tolkien", "1937")
book2 = Book("1984", "Orwell", "1980")

print(book1.describe())
print(book2.describe())

# =============================================================================
# EXERCISE 2 🟢 — Add a method
# =============================================================================
# Add a method `describe()` to the Book class that returns a string like:
#   "'The Hobbit' by Tolkien (published 1937)"
#
# Update __init__ to also take `year`. Test describe() on two books.


# YOUR CODE HERE
# Done in ex1



# =============================================================================
# EXERCISE 3 🟡 — Counter (class attribute as shared state)
# =============================================================================
# Write a class `Counter` such that every time an instance is created, a
# class-level counter increments. Do not add any parameters to __init__.
#
# Expected behavior:
#   c1 = Counter()
#   c2 = Counter()
#   c3 = Counter()
#   print(Counter.count)  # 3
#
# HINT: You need a class attribute AND you need to increment it from __init__.
# Think carefully: should it be `self.count += 1` or `Counter.count += 1`?
# Try both and see what happens.


class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

c1 = Counter()
c2 = Counter()
c3 = Counter()
print(Counter.count)  # 3
    


# =============================================================================
# EXERCISE 4 🔴 — PREDICT BEFORE RUNNING
# =============================================================================
# Look at this code. Write your PREDICTED output as a comment before running it.
# Then run it and compare.

class Config:
    debug = False

c = Config()
print(c.debug)        # YOUR PREDICTION: False
c.debug = True
print(c.debug)        # YOUR PREDICTION: True
print(Config.debug)   # YOUR PREDICTION: True

d = Config()
print(d.debug)        # YOUR PREDICTION: True

# After running, if you got anything wrong, write a 1-line explanation for
# yourself. The `d.debug` line is the one most people get wrong.


# YOUR CODE HERE (copy the code above, add predictions, then uncomment to run)

# I was wrong about print(Config.debug) and d = Config()
# print(d.debug)   Let me investigate it

# OK let me explain why I was thinking in that way. First of all, I thought, that as class attirbutes are shared,
# and we did change it as c.debug = True, I thought this will reflect to Config.debug, coz I thought c.debug = True will change
# value for all.

# So now, I understand, so when I do Condig.debug Python looks in Config.__dict__ directly, there is no instance to check


# =============================================================================
# EXERCISE 5 🔴 — REPRODUCE THE TRAP
# =============================================================================
# Write a class `Student` with:
#   - A CLASS attribute `grades = []`  (mutable — wrong on purpose)
#   - An __init__ that takes `name` and stores it as an instance attribute
#   - A method `add_grade(grade)` that does `self.grades.append(grade)`
#
# Then run:
#   s1 = Student("Alice")
#   s2 = Student("Bob")
#   s1.add_grade(95)
#   print(f"{s1.name}: {s1.grades}")
#   print(f"{s2.name}: {s2.grades}")
#
# OBSERVE THE BUG. Do not fix it yet. Just look at what printed.
# Write a comment explaining WHY Bob has a grade he never added.


# YOUR CODE HERE

class Student:
    grades = [] # Classs attribute

    def __init__(self, name):
        self.name = name # Instance attribute

    
    def add_grade(self, grade):
        self.grades.append(grade)

    

# s1 = Student("Alice")
# s2 = Student("Bob")
# s1.add_grade(95)
# print(f"{s1.name}: {s1.grades}")
# print(f"{s2.name}: {s2.grades}")

# I will explain the BUG. So why it happened, is that, we are using class attribute, which is shared accross class. So 
# each object does not have it's own attribute, instead the got shared, same one, that;s why changes affecting both
# of the objects


# =============================================================================
# EXERCISE 6 🟡 — FIX THE TRAP
# =============================================================================
# Rewrite the Student class from Exercise 5 so each student has their OWN
# grades list. Verify the bug is gone by running the same test code.
#
# Also add a method `average()` that returns the average grade (or 0.0 if
# no grades yet).


# YOUR CODE HERE

class Student:

    def __init__(self, name):
        self.name = name
        self.grades = []
    
    def add_grade(self, grade):
        self.grades.append(grade)

    
    def average(self):
        if len(self.grades) == 0: #. Better way to check: if not self.grades
            return 0.0 # use None instead
        
        return sum(self.grades) / len(self.grades)
    

    def __repr__(self):
        return f"Student(name={self.name!r}, grades={self.grades})"

s1 = Student("Alice")
s2 = Student("Bob")
s1.add_grade(95)
s1.add_grade(23)
print(f"{s1.name}: {s1.grades}")
print(f"{s2.name}: {s2.grades}")

print(f"{s1.name}: {s1.grades}")
print(f"{s2.name}: {s2.grades}")
print(f"{s1.name}'s average: {s1.average()}")
print(f"{s2.name}'s average: {s2.average()}")
        


# =============================================================================
# EXERCISE 7 🟣 — BankAccount (real-world)
# =============================================================================
# Build the BankAccount class we described in the guide:
#
# Requirements:
#   - __init__ takes `owner` (string) and `initial_balance` (defaults to 0)
#   - Class attribute: `interest_rate = 0.02` (2% — shared across all accounts)
#   - Method `deposit(amount)`:
#       - If amount <= 0, raise ValueError("Deposit must be positive")
#       - Otherwise, add to balance
#   - Method `withdraw(amount)`:
#       - If amount <= 0, raise ValueError("Withdrawal must be positive")
#       - If amount > balance, raise ValueError("Insufficient funds")
#       - Otherwise, subtract from balance
#   - Method `apply_interest()`:
#       - Multiply balance by (1 + interest_rate)
#   - Method `__repr__(self)` that returns something like:
#       "BankAccount(owner='Alice', balance=1020.0)"
#
# Test:
#   alice = BankAccount("Alice", 1000)
#   alice.deposit(200)
#   alice.withdraw(100)
#   alice.apply_interest()
#   print(alice)  # should use your __repr__

#   try:
#       alice.withdraw(99999)
#   except ValueError as e:
#       print("Caught:", e)


# YOUR CODE HERE

class BankAccount:
    interest_rate = 0.02

    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.initial_balance = initial_balance

    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.initial_balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        elif amount > self.initial_balance:
            raise ValueError("Insufficient funds")
        self.initial_balance -= amount

    def apply_interest(self):
        self.initial_balance = self.initial_balance * (1 + self.interest_rate)


    def __repr__(self):
        return f"BankAcount=(owner: {self.owner}, balance: {self.initial_balance})"


alice = BankAccount("Alice", 1000)
alice.deposit(200)
alice.withdraw(100)
alice.apply_interest()
print(alice)  # should use your __repr__

try:
    alice.withdraw(99999)
except ValueError as e:
    print("Caught:", e)





# =============================================================================
# EXERCISE 8 🔴 — PREDICT BEFORE RUNNING (the trap, again, slightly disguised)
# =============================================================================
class Box:
    contents = []

    def __init__(self, name):
        self.name = name

    def add(self, item):
        self.contents.append(item)

a = Box("A")
b = Box("B")
a.add("apple")
b.add("banana")

print(a.contents)    # YOUR PREDICTION: apple, banana
print(b.contents)    # YOUR PREDICTION: apple, banana
#
# Run it. Then, in a comment, explain:
# 1. What prints?
# 2. Why?
# 3. How would you fix the class so a.contents == ['apple'] and b.contents == ['banana']?
#
# Finally, write the fixed version of the class below.

# Explanation: Same problem as above, so we using class methods, which are shared


# YOUR CODE HERE (predictions, then the broken code, then the fix)
class Box:


    def __init__(self, name):
        self.name = name
        self.contents = []

    def add(self, item):
        self.contents.append(item)

a = Box("A")
b = Box("B")
a.add("apple")
b.add("banana")

print(a.contents)   
print(b.contents) 




# =============================================================================
# EXERCISE 9 🟣 — ShoppingCart (real-world, combines everything)
# =============================================================================
# Build a ShoppingCart class with:
#
#   - Class attribute: `tax_rate = 0.08` (8% — shared)
#   - __init__ takes `owner`. Initializes `items = []` (list of dicts like
#     {"name": "shirt", "price": 25.00, "quantity": 2})
#
#   - Method `add_item(name, price, quantity=1)`:
#       - Appends a dict to self.items
#
#   - Method `remove_item(name)`:
#       - Removes the first item whose name matches
#       - If no match, raise ValueError(f"No item named {name}")
#
#   - Method `subtotal()`:
#       - Returns sum of price * quantity for all items
#
#   - Method `total()`:
#       - Returns subtotal * (1 + tax_rate)
#
#   - Method `__repr__(self)`:
#       - Returns "ShoppingCart(owner='Alice', items=3, total=$54.00)"
#         where items is the number of DISTINCT items (len of list) and
#         total is formatted to 2 decimal places.
#
# Test thoroughly:
#   cart = ShoppingCart("Alice")
#   cart.add_item("shirt", 25.00, 2)
#   cart.add_item("hat", 15.00)
#   print(cart.subtotal())  # 65.00
#   print(cart.total())     # 70.20
#   print(cart)             # uses __repr__
#   cart.remove_item("hat")
#   print(cart.subtotal())  # 50.00
#
#   try:
#       cart.remove_item("doesnotexist")
#   except ValueError as e:
#       print("Caught:", e)


# YOUR CODE HERE

class ShoppingCart:
    tax_rate = 0.08 # class method


    def __init__(self, owner):
        self.owner = owner
        self.items = list()

    def add_item(self, name, price, quantity=1):
        self.items.append({"name": name, "price": price, "quantity":quantity})


    def remove_item(self, name):
        for item in self.items:
            if item['name'] == name:
                self.items.remove(item)
                return
            raise ValueError(f"No item named {name}")
        
    def subtotal(self):
        total = 0.0
        for item in self.items:
            total += item['price'] * item['quantity']
        return total

       
        
    def total(self):
        return self.subtotal() * (1 + self.tax_rate)

    def __repr__(self):
        return f"ShoppingCart(owner={self.owner!r}, items={len(self.items)}, total=${self.total():.2f})"


cart = ShoppingCart("Alice")
cart.add_item("shirt", 25.00, 2)
cart.add_item("hat", 15.00)
print(cart.subtotal())  # 65.00
print(cart.total())     # 70.20
print(cart)             # uses __repr__
cart.remove_item("hat")
print(cart.subtotal())  # 50.00

try:
    cart.remove_item("doesnotexist")
except ValueError as e:
    print("Caught:", e)







# =============================================================================
# REFLECTION
# =============================================================================
# When you've finished all 10 exercises, take 2 minutes and answer these in
# comments at the bottom of the file:
#
# 1. Which exercise surprised you most? Why?
# 2. In your own words, when would you use a class attribute vs an instance
#    attribute?
# 3. What's the one-line rule you'll remember to avoid the mutable class
#    attribute trap?


# 1. I was really surprised by the last exercise, which is ex 9. Because, I needed to use dict/list manipulations
# 2. I will use class attribute when definign fixed value thins and things that can be shated across all instances
# 3. The mutables (list, dict, set) always goes to __init__ constructor





