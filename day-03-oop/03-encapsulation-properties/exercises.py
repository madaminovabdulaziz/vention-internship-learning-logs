"""
Day 3 · Part 3 — Exercises: Encapsulation & Properties

HOW TO USE:
1. Work in order.
2. For 🔴 PREDICT exercises, write your prediction as a comment BEFORE running.
3. Commit when done:
   git add day-03-oop/03-encapsulation-properties/
   git commit -m "day-03 part 3: encapsulation & properties"

DIFFICULTY LEGEND:
  🟢 = Warm-up
  🟡 = Applied
  🔴 = Predict before running
  🟣 = Real-world
"""

# =============================================================================
# EXERCISE 1 🟢 — Three levels of access (observe, don't fight it)
# =============================================================================
# Write a class SecretBox with three attributes set in __init__:
#
#   - self.public_data = "anyone can see"
#   - self._protected_data = "friends only"
#   - self.__private_data = "truly mine"
#
# Then, OUTSIDE the class, try to access each one from an instance:
#   - box.public_data         → should work
#   - box._protected_data     → should work (Python doesn't actually stop you)
#   - box.__private_data      → should FAIL with AttributeError
#
# After the AttributeError, figure out the mangled name (hint: _ClassName__attr)
# and access the "private" attribute through that name. Prove that "private"
# in Python isn't really private — just harder to reach.


# YOUR CODE HERE

class SecretBox:
    def __init__(self):
        self.public_data = "anyone can see"
        self._protected_data = "friends only"
        self.__private_data = "truly mine"


box = SecretBox()

print(box.public_data)
print(box._protected_data)
print(box._SecretBox__private_data)

# =============================================================================
# EXERCISE 2 🟡 — Protected convention in practice
# =============================================================================
# Build a Logger class:
#
#   - __init__(self, name): stores self.name (public)
#   - Stores self._messages = []  (protected — internal buffer)
#   - Method log(message): appends to self._messages
#   - Method show(): prints all messages numbered 1, 2, 3...
#
# Test:
#   logger = Logger("app")
#   logger.log("started")
#   logger.log("connected")
#   logger.show()
#   # 1. started
#   # 2. connected
#
# Notice: you CAN do `logger._messages.append("hack")` from outside. Python
# doesn't stop you. The _ is a contract, not a lock. Write a comment at the
# bottom explaining why we use _messages instead of just messages.


# YOUR CODE HERE

class Logger:
    def __init__(self, name):
        self.name = name
        self._messages = []


    def log(self, message):
        self._messages.append(message)
    
    def show(self):
        print(self._messages)

logger = Logger("app")
logger.log("started")
logger.log("connected")
logger.show()
# 1. started
# 2. connected


# =============================================================================
# EXERCISE 3 🟢 — Your first @property
# =============================================================================
# Build a Circle class with:
#
#   - __init__(self, radius): stores self._radius
#   - @property radius → returns self._radius
#   - (no setter yet — read-only)
#
# Test:
#   c = Circle(5)
#   print(c.radius)    # 5  (notice: no parens, even though radius is a method)
#
#   try:
#       c.radius = 10   # should fail
#   except AttributeError as e:
#       print("Caught:", e)


# YOUR CODE HERE

class Circle:
    def __init__(self, radius):
        self._radius = radius

    
    @property
    def radius(self):
        return self._radius
    
# c = Circle(5)
# print(c.radius)    # 5  (notice: no parens, even though radius is a method)

# try:
#     c.radius = 10   # should fail
# except AttributeError as e:
#     print("Caught:", e)



# =============================================================================
# EXERCISE 4 🟡 — Add a setter with validation
# =============================================================================
# Extend the Circle class from Ex 3:
#
#   - Add @radius.setter that:
#       - Raises TypeError if value is not a number (int or float)
#       - Raises ValueError if value is negative or zero
#       - Otherwise, sets self._radius = value
#
# Test:
#   c = Circle(5)
#   c.radius = 10          # works
#   print(c.radius)        # 10
#
#   try:
#       c.radius = -5       # ValueError
#   except ValueError as e:
#       print("Caught:", e)
#
#   try:
#       c.radius = "big"    # TypeError
#   except TypeError as e:
#       print("Caught:", e)


# YOUR CODE HERE


class Circle:
    def __init__(self, radius):
        self._radius = radius

    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if isinstance(value, (int, float)):
            raise TypeError("NaN")
        if value <= 0:
            raise ValueError("I need non zero")
        self._radius = value
    
c = Circle(5)
c.radius = 10          # works
print(c.radius)        # 10

try:
    c.radius = -5       # ValueError
except ValueError as e:
    print("Caught:", e)

try:
    c.radius = "big"    # TypeError
except TypeError as e:
    print("Caught:", e)


# =============================================================================
# EXERCISE 5 🟡 — Computed property (read-only)
# =============================================================================
# Extend the Circle class further:
#
#   - Class attribute: PI = 3.14159
#   - @property area → returns PI * radius**2
#   - @property diameter → returns 2 * radius
#   - @property circumference → returns 2 * PI * radius
#
# None of these have setters — they're all read-only computed properties.
#
# Test:
#   c = Circle(5)
#   print(c.area)            # 78.53975
#   print(c.diameter)        # 10
#   print(c.circumference)   # 31.4159
#
#   c.radius = 10
#   print(c.area)            # 314.159 — stays in sync with radius automatically


# YOUR CODE HERE


# =============================================================================
# EXERCISE 6 🔴 — PREDICT: the infinite recursion trap
# =============================================================================
# Look at this code. Will it work? What will happen?
#
# class Broken:
#     def __init__(self, value):
#         self.value = value       # note: NOT self._value
#
#     @property
#     def value(self):
#         return self.value        # hmmm...
#
#     @value.setter
#     def value(self, v):
#         self.value = v           # hmmm...
#
# b = Broken(5)
#
# YOUR PREDICTION (before running):
#   - Does `Broken(5)` succeed? Why or why not?
#   - If it crashes, what error?
#
# After predicting, run it. Understand exactly what went wrong.
# Then fix the class (use self._value for storage) and test:
#   b = Broken(5)
#   print(b.value)    # 5
#   b.value = 10
#   print(b.value)    # 10


# YOUR PREDICTION, THEN THE FIXED VERSION HERE


# =============================================================================
# EXERCISE 7 🟣 — BankAccount with properties (REWRITE)
# =============================================================================
# Rewrite the BankAccount class from Part 1 using properties:
#
#   - __init__(self, owner, initial_balance=0)
#   - owner is a public attribute
#   - Storage: self._balance
#
#   - @property balance → returns self._balance
#   - @balance.setter:
#       - TypeError if not int/float
#       - ValueError if negative
#       - Otherwise sets self._balance
#
#   - Method deposit(amount): uses self.balance = self.balance + amount
#     (through the property, so validation runs)
#   - Method withdraw(amount):
#       - ValueError if amount <= 0: "Withdrawal must be positive"
#       - ValueError if amount > self.balance: "Insufficient funds"
#       - Otherwise self.balance -= amount
#
#   - __repr__ → "BankAccount(owner='Alice', balance=1000.0)"
#
# Test:
#   alice = BankAccount("Alice", 1000)
#   print(alice.balance)        # 1000  (via property getter)
#   alice.deposit(500)
#   print(alice.balance)        # 1500
#
#   try:
#       alice.balance = -10     # through setter — ValueError
#   except ValueError as e:
#       print("Caught:", e)
#
#   try:
#       alice.balance = "hi"    # through setter — TypeError
#   except TypeError as e:
#       print("Caught:", e)
#
# Notice how deposit/withdraw now go THROUGH the property, automatically
# validating every change. That's the power of properties — you enforce
# rules in one place and all code paths benefit.


# YOUR CODE HERE


# =============================================================================
# EXERCISE 8 🟣 — Temperature with linked properties (the elegant demo)
# =============================================================================
# Build a Temperature class where celsius and fahrenheit are BOTH properties,
# but only ONE is actually stored:
#
#   - __init__(self, celsius)
#   - Storage: self._celsius
#
#   - @property celsius → returns self._celsius
#   - @celsius.setter: sets self._celsius (no validation needed for this ex)
#
#   - @property fahrenheit → COMPUTED from self._celsius
#       - formula: celsius * 9/5 + 32
#   - @fahrenheit.setter → when set, UPDATES self._celsius
#       - formula: self._celsius = (value - 32) * 5/9
#
# This is the elegant part: whether the caller sets celsius or fahrenheit,
# there's only one source of truth — self._celsius. They're always in sync.
#
# Test:
#   t = Temperature(100)
#   print(t.celsius)        # 100
#   print(t.fahrenheit)     # 212.0
#
#   t.fahrenheit = 32
#   print(t.celsius)        # 0.0
#   print(t.fahrenheit)     # 32.0
#
#   t.celsius = -40
#   print(t.fahrenheit)     # -40.0  (fun fact: -40 is the same in both scales)


# YOUR CODE HERE


# =============================================================================
# EXERCISE 9 🟣 — User with email normalization (the refactoring killer app)
# =============================================================================
# Build a User class that demonstrates WHY properties are amazing for
# adding rules after the fact.
#
# Phase 1: Write the naive version first (NO properties):
#   class User:
#       def __init__(self, name, email):
#           self.name = name
#           self.email = email
#
# Create a user and print its email. Notice nothing normalizes or validates.
#
# Phase 2: Now refactor to use a property for email:
#   - Storage: self._email
#   - @property email: returns self._email
#   - @email.setter:
#       - Raise ValueError if "@" not in value
#       - Otherwise: store value.strip().lower()
#
# Note: your __init__ line `self.email = email` should NOT change. Because
# it's now going through the setter, the normalization happens automatically.
#
# Test (Phase 2):
#   u = User("Alice", "  Alice@Example.COM  ")
#   print(u.email)           # alice@example.com  (stripped + lowered)
#
#   try:
#       u.email = "not-an-email"
#   except ValueError as e:
#       print("Caught:", e)
#
# The magic: you added validation + normalization WITHOUT changing the
# calling code in __init__. That's the whole selling point of properties.


# YOUR CODE HERE (Phase 1 and Phase 2, both)


# =============================================================================
# EXERCISE 10 🔴 — PREDICT: public vs property
# =============================================================================
# class A:
#     def __init__(self):
#         self.x = 10
#
# class B:
#     def __init__(self):
#         self._x = 10
#     @property
#     def x(self):
#         return self._x
#
# a = A()
# b = B()
#
# For EACH of these, predict the result — works or raises?
#
# print(a.x)              # PREDICTION:
# print(b.x)              # PREDICTION:
# a.x = 99                # PREDICTION:
# b.x = 99                # PREDICTION:   ← tricky
# print(a.x)              # PREDICTION:
# print(b.x)              # PREDICTION:
#
# The tricky one: `b.x = 99`. Does it work? Why or why not?
# Write your reasoning before running. Then run and verify.
#
# After running, in a comment, explain: what's the difference between
# a public attribute and a property WITHOUT a setter?


# YOUR CODE HERE


# =============================================================================
# REFLECTION
# =============================================================================
# When you've finished, answer in comments:
#
# 1. In your own words: when should you reach for a @property instead of
#    a plain public attribute?
#
# 2. Why do we store data in `self._x` when the property is `self.x`?
#    What goes wrong if we use the same name?
#
# 3. Name one real-world class (from a library you've used or can imagine)
#    where properties would make sense. Explain in 2 sentences.