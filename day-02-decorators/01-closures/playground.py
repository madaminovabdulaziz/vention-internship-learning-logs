def make_greeter(name):
    def greet():
        print(f"Hello! {name}")
    return greet

greet_alice = make_greeter("ALICE")
greet_bob = make_greeter('BOBBEK!')


print(greet_alice.__closure__)


################################


def make_button(label, message):
    def on_click():
        print(f"[{label}] {message}!")
    return on_click

save_btn = make_button("SAVE", "File Saved")
delete_btn = make_button("DELETE", "File Deleted")

save_btn()
delete_btn()


#######################

def outer():
    x = 10
    def inner():
        nonlocal x
        x = x + 1
        print(x)
    inner()

outer()


##############

def outer():
    def inner():
        return "Hi"
    return inner


print(outer) # Error
print(outer()) # Hi
print(outer()()) # Do not know


funcs = []
for i in range(3):
    def f():
        return i
    funcs.append(f)

print(funcs)


funcs = []

for name in ["alice", "bob", "carol"]:

    def greeter():

        print(f"Hello, {name}!")

    funcs.append(greeter)

funcs[0]()

funcs[1]()

funcs[2]()


def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

# double = make_multiplier(5)
# print(double(2))


print(make_multiplier)          # what is this? -> some adress
print(make_multiplier(5))       # what is this? -> some adress
print(make_multiplier(5)(2))    # what is this? 10

double = make_multiplier(5)
print(double)                   # what is this?
print(double(2))                # what is this?
print(double(3))                # what is this?
print(double(10))               # what is this?