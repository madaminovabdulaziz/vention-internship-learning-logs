
first_list = [1, 2, 4]
second_list = [5, 6, 7]


def all_items():
    for x in first_list:
        yield  x
    for y in second_list:
        yield  y



for i in all_items():
    print(i)


print(type(all_items()))