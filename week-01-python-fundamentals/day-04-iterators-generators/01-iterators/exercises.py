class Countdown:
    def __init__(self, start):
        self.current = start


    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        
        value = self.current
        self.current -= 1

        return value
    

for n in Countdown(3):
    print(n)



class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0


    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.current:
            raise StopIteration
        value = self.current
        self.current +=2
        return value
    

    
for n in EvenNumbers(10):
    print(n)



class Countdown:
    def __init__(self, start):
        self.current = start

    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1

        return value
        





class CDown:
    def __init__(self, initial):
        self.value = initial

    def __iter__(self):
        return  self
        
    def __next__(self):
        if self.value == 0:
            raise StopIteration
        
        value = self.value
        self.value -= 1
        return value




for i in CDown(5):
    print(i)



def countdown(num):
    while num > 0:
        yield num
        num -= 1

    



for i in countdown(10):
    print(i)