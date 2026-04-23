class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficent funds")
        self.balance -= amount

        
# alice = BankAccount("Alice", 1000)
# alice.deposit(200)
# print(alice.balance)  # 1200

# alice.withdraw(5000) 




class Dog:
    def bark(self):
        print(f"{self.name} says woof!")

rex = Dog()
rex.name = "Rex"

# These two lines do EXACTLY the same thing:
rex.bark()          # Rex says woof!
Dog.bark(rex)       # Rex says woof!
        

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author


#     def describe(self):
#         return "Good book to read"

    


# book1 = Book("1984", "George Orwell")
# book2 = Book("Why We Sleep", "Mathew Walker")

# print(book1.title, book1.author)
# print(book2.title, book2.author)
# print(book1.describe())




# class Counter:
#     def __init__(self):
#         self.counter = 0

#     def count(self):
#         self.counter = self.counter + 1
#         return self.counter

    
    
    

# c1 = Counter()
# c2 = Counter()
# c3 = Counter()
# print(Counter.count) 




class Config:
    debug = False

c = Config()
c.debug = True

print(c.__dict__)          # {'debug': True}  ← c's own attribute
print(Config.__dict__)     # {..., 'debug': False, ...}  ← untouched

# Delete c's instance attribute and watch the class one reappear
del c.debug
print(c.debug)             # False — no instance attr, falls through to class