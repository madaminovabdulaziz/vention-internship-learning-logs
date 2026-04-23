"""
Day 3 · Part 2 — Exercises: Methods (Instance, Class, Static) + Basic Dunders

HOW TO USE THIS FILE:
1. Work in order. Each exercise builds on the previous ones.
2. For 🔴 "PREDICT" exercises, write your prediction as a comment BEFORE running.
3. Commit when done:
   git add day-03-oop/02-methods/
   git commit -m "day-03 part 2: methods (instance, class, static) + dunders"

DIFFICULTY LEGEND:
  🟢 = Warm-up (syntax drill)
  🟡 = Applied (use the concept for something useful)
  🔴 = Predict before running
  🟣 = Real-world (production-flavored)
"""

import datetime

time = datetime.datetime.now()

# =============================================================================
# EXERCISE 1 🟢 — Classmethod as alternative constructor
# =============================================================================
# Build a Date class:
#
#   - __init__ takes year, month, day (ints) and stores them
#   - @classmethod from_string(cls, date_str):
#       - Parses "YYYY-MM-DD" strings
#       - Returns a new Date instance
#       - Hint: use date_str.split("-") and map(int, ...) or a list comprehension
#   - __repr__ returns "Date(year=2024, month=1, day=15)"
#
# Test:
#   d1 = Date(2024, 1, 15)
#   d2 = Date.from_string("2024-01-15")
#   print(d1)
#   print(d2)


# YOUR CODE HERE

class Date:
    def __init__(self, year, month, day: int):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_str: str):
        parts = [int(x) for x in date_str.split('-')]
        print(parts)
        return cls(*parts)
    
    @staticmethod
    def is_leap_year(year: int):
        if year % 4 == 0 and year % 400 == 0:
            return True
        return False

    
    def __repr__(self):
        return f"Date(year={self.year}, month={self.month}, day={self.day})"
    
# Test:
d1 = Date(2024, 1, 15)
d2 = Date.from_string("2024-01-15")
print(d1)
print(d2)



# =============================================================================
# EXERCISE 2 🟢 — Staticmethod for validation
# =============================================================================
# Extend the Date class above with:
#
#   - @staticmethod is_leap_year(year) that returns True if year is a leap year
#     (divisible by 4, except centuries not divisible by 400)
#     - 2000 → True
#     - 2024 → True
#     - 1900 → False
#     - 2023 → False
#
# Why is this a @staticmethod and not a @classmethod?
# Answer in a comment below the method.
#
# Test:
print(Date.is_leap_year(2000))   # True
print(Date.is_leap_year(1900))   # False
print(Date.is_leap_year(2024))   # True
print(Date.is_leap_year(2023))   # False


# YOUR CODE HERE




# =============================================================================
# EXERCISE 3 🟡 — Counting instances (classmethod reading class state)
# =============================================================================
# Build a User class that tracks how many users have been created.
#
#   - Class attribute: count = 0
#   - __init__ takes name; increments User.count
#   - @classmethod total_users(cls) → returns cls.count
#   - @classmethod reset(cls) → sets cls.count back to 0 (for testing)
#
# Test:
#   print(User.total_users())  # 0
#   u1 = User("Alice")
#   u2 = User("Bob")
#   u3 = User("Carol")
#   print(User.total_users())  # 3
#   User.reset()
#   print(User.total_users())  # 0


# YOUR CODE HERE


class User:
    count = 0

    def __init__(self, name):
        self.name = name
        User.count += 1

    @classmethod
    def total_users(cls):
        return cls.count
    
    @classmethod
    def reset(cls):
        cls.count = 0
        

print(User.total_users())  # 0
u1 = User("Alice")
u2 = User("Bob")
u3 = User("Carol")
print(User.total_users())  # 3
User.reset()
print(User.total_users())  # 0



# =============================================================================
# EXERCISE 4 🔴 — PREDICT: who can call what?
# =============================================================================
class Widget:
    count = 0

    def __init__(self, name):
        self.name = name
        Widget.count += 1

    def describe(self):
        return f"Widget({self.name})"

    @classmethod
    def total(cls):
        return cls.count

    @staticmethod
    def is_valid_name(name):
        return isinstance(name, str) and len(name) > 0

w = Widget("gear")
#
# # For EACH of these, predict: does it work or raise? If it works, what prints?
#
# print(w.describe())             # PREDICTION: gear
# print(Widget.describe(w))       # PREDICTION: gear
# print(Widget.total())           # PREDICTION: 3
# print(w.total())                # PREDICTION:  4  ← tricky!
# print(Widget.is_valid_name("x"))# PREDICTION: True
# print(w.is_valid_name("y"))     # PREDICTION:  True ← also tricky!
# print(Widget.describe())        # PREDICTION:  no ← will this work?
#
# The last three are the learning ones. Predict all seven, then run.
# After running, explain in a comment: what do the "tricky" ones teach about
# how Python dispatches method calls?


# So let me tell my reflections, why I was wrong etc.
# So the thing is, I predicted first one correct, but second one I failed, i thought, that describe(self) method 
# takes 0 arguments, byt we are giving class itself, it is wrong, so now I realized, that Widget.desribe(w) is equal to
# w.describe()

#A Another error I made is I thought, whenever we declare a class, it will increment count, but count increments only when
# class initializes, coz it initialized only once in w = Widget(w)






# =============================================================================
# EXERCISE 5 🟣 — Temperature class (the full picture)
# =============================================================================
# Build a Temperature class that handles Celsius ↔ Fahrenheit conversion.
#
#   - __init__ takes celsius (float) and stores it as self.celsius
#   - Instance method to_fahrenheit(self) → returns celsius * 9/5 + 32
#   - @classmethod from_fahrenheit(cls, f) → converts and returns a new Temperature
#   - @staticmethod is_freezing(celsius) → returns True if celsius <= 0
#   - @staticmethod is_boiling(celsius) → returns True if celsius >= 100
#   - __repr__ → "Temperature(celsius=25.0)"
#   - __eq__ → two temperatures are equal if their celsius values match
#
# Test:
#   t1 = Temperature(25)
#   print(t1.to_fahrenheit())              # 77.0
#
#   t2 = Temperature.from_fahrenheit(77)
#   print(t2.celsius)                       # 25.0
#   print(t1 == t2)                         # True ← tests __eq__
#
#   print(Temperature.is_freezing(-5))     # True
#   print(Temperature.is_boiling(105))     # True
#
#   print(t1)                               # uses __repr__


class Temperature:
    def __init__(self, celsius: float):
        self.celsius = float(celsius)


    def to_fahrenheit(self):
        return self.celsius * 9/5 + 32
    

    @classmethod
    def from_fahrenheit(cls, f):
        celsius = (f-32) * 5/9
        return cls(celsius)
    

    @staticmethod
    def is_freezing(celsius):
        return celsius <= 0
    
    @staticmethod
    def is_boiling(celcius):
        return celcius >= 100
    

    def __repr__(self):
        return f"Temperature(celsus={self.celsius})"
    
    def __eq__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.celsius == other.celsius

t1 = Temperature(25)
print(t1.to_fahrenheit())              # 77.0

t2 = Temperature.from_fahrenheit(77)
print(t2.celsius)                       # 25.0
print(t1 == t2)                         # True ← tests __eq__

print(Temperature.is_freezing(-5))     # True
print(Temperature.is_boiling(105))     # True

print(t1)         



# =============================================================================
# EXERCISE 6 🟣 — Alternative constructors (the classic pattern)
# =============================================================================
# Build a User class with THREE ways to create a user:
#
#   - __init__(self, name, email, age)
#   - @classmethod from_dict(cls, data):
#       - data is a dict like {"name": "Alice", "email": "a@b.com", "age": 30}
#       - Return cls(data["name"], data["email"], data["age"])
#   - @classmethod from_csv(cls, csv_line):
#       - csv_line is a string like "Alice,a@b.com,30"
#       - Parse and return a new User
#       - age must be converted to int
#   - __repr__ → "User(name='Alice', email='a@b.com', age=30)"
#
# Test:
#   u1 = User("Alice", "a@b.com", 30)
#   u2 = User.from_dict({"name": "Bob", "email": "b@b.com", "age": 25})
#   u3 = User.from_csv("Carol,c@b.com,28")
#   print(u1)
#   print(u2)
#   print(u3)
#
# Bonus: which of these three ways to create a User is more useful in
# real code? (No code, just a 1-line comment.)


class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age


    @classmethod
    def from_dict(cls, data: dict):
        return cls(data['name'], data['email'], int(data['age']))
    

    @classmethod
    def from_csv(cls, data: str):
        parts = data.split(",")
        return cls(parts[0], parts[1], int(parts[2]))
    

    def __repr__(self):
        return f"User(name={self.name}, email={self.email}, age={self.age})"
    
u1 = User("Alice", "a@b.com", 30)
u2 = User.from_dict({"name": "Bob", "email": "b@b.com", "age": 25})
u3 = User.from_csv("Carol,c@b.com,28")
print(u1)
print(u2)
print(u3)

# from_dict is the most common in real code — any data crossing into a Python
#  process (HTTP requests, database rows, config files) arrives dict-shaped.





# =============================================================================
# EXERCISE 7 🔴 — PREDICT: which is @classmethod vs @staticmethod?
# =============================================================================
# For each of these, say whether it should be an instance method,
# @classmethod, or @staticmethod. Write your answer as a comment BEFORE
# checking below. No code yet — just think.
#
# Scenario A: A method on BankAccount that returns the current balance.
#   → YOUR ANSWER: staticmethod NOTE: WRONG! It should be instance method
#
# Scenario B: A method on Date that creates a Date from a unix timestamp.
#   → YOUR ANSWER: classmethod True
#
# Scenario C: A method on EmailValidator that checks if a string looks
#             like a valid email format (no instance state needed).
#   → YOUR ANSWER: staticmethod True
#
# Scenario D: A method on User that returns how many users have been created.
#   → YOUR ANSWER: classmethod True
#
# Scenario E: A method on ShoppingCart that computes tax on the cart's items.
#   → YOUR ANSWER:  staticmethod NOTE: WRONG! It should be instance method
#
# Scenario F: A method on Circle that returns the value of π (pi).
#   → YOUR ANSWER: staticmethod True
#
# Scenario G: A method on User that creates a User from an HTTP request body
#             (a dict).
#   → YOUR ANSWER: classmethod True
#
# Scenario H: A method on Geometry that computes the distance between two
#             points (takes two tuples, returns a float, doesn't care about
#             any class state).
#   → YOUR ANSWER: staticmethod True
#
# After answering all 8, check against the answer key at the BOTTOM of this file.
# For any you got wrong, explain the reasoning for the correct answer in a
# comment. This is the single most important exercise in the file.


# YOUR ANSWERS HERE


# =============================================================================
# EXERCISE 8 🟣 — Dunder practice: Money class
# =============================================================================
# Build a Money class that represents an amount in a currency.
#
#   - __init__(self, amount, currency="USD")
#       - amount should be a number (int or float)
#       - currency is a 3-letter code (default "USD")
#   - __repr__ → "Money(amount=100.0, currency='USD')"
#   - __str__  → "$100.00 USD"   (use {:.2f} for the amount format)
#   - __eq__   → two Money objects are equal if amount AND currency match
#                (Money(100, "USD") == Money(100, "EUR") should be False)
#
# Test:
#   m1 = Money(100)
#   m2 = Money(100, "USD")
#   m3 = Money(100, "EUR")
#   print(repr(m1))         # Money(amount=100, currency='USD')
#   print(str(m1))          # $100.00 USD
#   print(m1 == m2)         # True
#   print(m1 == m3)         # False  (different currency)
#   print(m1 == "100")      # False  (not even a Money object)


# YOUR CODE HERE

class Money:
    def __init__(self, amount, currency="USD"):
        self.amount = float(amount)
        self.currency = currency


    def __repr__(self):
        return f"Money(amount={self.amount}, currency={self.currency})"
    

    def __str__(self):
        return f"${self.amount:.2f} {self.currency}"
    
    def __eq__(self, value):
        if not isinstance(value, Money):
            return NotImplemented
        return self.amount == value.amount and self.currency == value.currency



m1 = Money(100)
m2 = Money(100, "USD")
m3 = Money(100, "EUR")
print(repr(m1))         # Money(amount=100, currency='USD')
print(str(m1))          # $100.00 USD
print(m1 == m2)         # True
print(m1 == m3)         # False  (different currency)
print(m1 == "100")      # False  (not even a Money object)


# =============================================================================
# REFLECTION
# =============================================================================
# When you've finished all 8, answer these in comments below:
#
# 1. In your own words, what's the ONE thing that makes you pick
#    @classmethod over @staticmethod?

# Ok, I will pick classmethod when I will do operations related to class itself
# I will choose staticmethods when I need to do operations not related to class, I mean independent
#
# 2. Give an example from real code (doesn't have to be yours — could be from
#    a library you've used) where @classmethod makes sense.

# datetime.now()
#
# 3. When would you NOT use @staticmethod, even if the function fits the
#    criteria? (hint: reread Section 4 of the guide)


# If the method is not referencing any class level data, I probably should not use a class at all