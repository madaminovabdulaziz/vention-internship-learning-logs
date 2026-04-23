my_list = [1, 2, 3, 4]

for x in my_list:
    print(x)



it = iter(my_list)
while True:
    try:
        x = next(it)
    except StopIteration:
        break

    print(x)