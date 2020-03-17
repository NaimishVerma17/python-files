import random

print(random.choice(range(100)))
print(random.choice([1, 2, 3, 4]))
print(random.choice("Random number"))
print(random.randrange(3, 10, 3))
print(random.random())  # Between 0 and 1

var_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(var_list)  # Shuffles the list
print(var_list)
