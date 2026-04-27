class Warrior:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def is_alive(self):
        return self.health > 0
    
    def take_damage(self, amount):
        self.health = max(0, self.health - amount)
    
    def attack_with_sword(self, target):
        target.take_damage(20)


class Mage:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def is_alive(self):
        return self.health > 0
    
    def take_damage(self, amount):
        self.health = max(0, self.health - amount)
    
    def cast_fireball(self, target):
        target.take_damage(30)


class Archer:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def is_alive(self):
        return self.health > 0
    
    def take_damage(self, amount):
        self.health = max(0, self.health - amount)
    
    def shoot_arrow(self, target):
        target.take_damage(15)



class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def is_alive(self):
        return self.health > 0
    
    def take_damage(self, amount):
        self.health = max(0, self.health - amount)


class Warrior(Character):            # ← "Warrior IS A Character"
    def attack_with_sword(self, target):
        target.take_damage(20)


class Mage(Character):               # ← "Mage IS A Character"
    def cast_fireball(self, target):
        target.take_damage(30)


class Archer(Character):             # ← "Archer IS A Character"
    def shoot_arrow(self, target):
        target.take_damage(15)


w = Warrior("Conan", 100)
print(w.name)              # "Conan" — inherited from Character's __init__
print(w.is_alive())         # True — inherited from Character's is_alive method
w.take_damage(30)           # inherited from Character
print(w.health)             # 70
w.attack_with_sword(w)      # Warrior's own method



# In this case, all methods from base class (parent) class inherited, including (__init__)
# all class attributes from the parent

class Emlpoyee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        if amount < 0:
            raise ValueError("Raise cannot be negative")
        self.salary += amount

    
    def annual_bonus(self):
        return self.salary * 0.05
    
    def __repr__(self):
        return f"Employee(name={self.name}, salary={self.salary})"
    


    