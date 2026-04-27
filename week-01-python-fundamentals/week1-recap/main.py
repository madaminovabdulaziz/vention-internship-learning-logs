# 1) SLICING reflex


s = "Python Tricks"

reversed_string = s[::-1]

every_other_char = s[::2]

last_4_chars = s[-4:]

drop_first_last = s[1:-2]

print(reversed_string)
print(every_other_char)
print(last_4_chars)
print(drop_first_last)


# 2) sort vs sorted


words = ["banana", "Apple", "cherry"]

# print(sorted(words, key=str.lower))


words.sort()
print(words)



# List comprehensions


ex1 = [x*x for x in range(1, 20) if x % 2 == 1]
print(ex1)

sentence = ['hi', 'hello', 'hey']

ex2 = {w: len(w) for w in sentence}


prg = "programming"

ex3 = {char for char in prg if char in "aeiou"}

print(ex3)



# DICT iteration
scores = {"alice": 90, "bob": 75, "carol": 88}

scores.get('bob' , 0)

result = {k: v for k, v in scores.items() if k == "bob"}
