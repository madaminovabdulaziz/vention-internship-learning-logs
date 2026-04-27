def add_item(item, my_list=None):

    my_list = []
    my_list.append(item)
    return my_list

print(add_item(1))  # [1]
print(add_item(2))  # [2]  ← fresh list each call
print(add_item(3))  # [3]