def countdown(n):
    while n > 0:
        yield n
        n -= 1

for x in countdown(5):
    print(x)
# 5 4 3 2 1

# print(list(countdown(3)))   # [3, 2, 1]