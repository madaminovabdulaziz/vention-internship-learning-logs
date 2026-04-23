# class User:
#     def __init__(self, name):
#         self.name = name
#         self._session_token = None # Protected -> internal use
#         self.__password = "secret"

#     def login(self, token):
#         self._session_token = token


#     def check_password(self, attempt):
#         return attempt == self.__password
    

    
# Properties

class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self._balance = initial_balance

    @property
    def balance(self):
        return self._balance
    

    @balance.setter
    def balance(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Balance must be a number")
        
        if value < 0:
            raise ValueError("Balance cannot be negative")
        
        self._balance = value



alice = BankAccount("Alice")

alice.balance = 798

# alice.get_balance() # ugly
# alice.set_balance(10000)  # also ugly


print(alice.balance)




class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    
    @property
    def area(self):
        return self.width * self.height
    

    @property
    def perimeter(self):
        return 2 * (self.height + self.width)



r = Rectangle(3, 4)

print(r.area)
print(r.perimeter)

r.width = 10
print(r.area)





### Property deleter

class User:
    def __init__(self, name):
        self._name = name # private

    
    @property
    def name(self):
        return self._name
    


    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        
        self._name = value

    

    @name.deleter
    def name(self):
        print("Deleting name")
        self._name = None


u = User("Alice")
del u.name          # "Deleting name..."
print(u.name)       # None



class HumanUser:
    def __init__(self, email):
        self.email = email

    
    @property
    def email(self):
        return self._email
    

    @email.setter
    def email(self, value: str):
        if "@" not in value:
            raise ValueError("Invalid email")
        self._email = value.lower()
    