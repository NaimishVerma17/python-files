# Numbers

# num1 and num2 both are different
num1 = 12  # int
num2 = 12.0  # float

# Strings

str1 = 'This is a string!'
print(str1)
print(str1[1])
print(str1[1:5])
print(str1[1:])
print(str1[:3])
print(str1[:])

# Lists

list_one = [1, 'one', True, 4]
print(list_one)

list_two = [2, 'two', False, 4]
print(list_two)

print(list_two * 2)  # Duplicate the list
print(list_one + list_two)  # merge two lists

list_two[0] = True  # Mutation and assignment
print(list_two)

# Tuples

tuple_one = (1, 'one', True, 4)
print(tuple_one)

tuple_two = (2, 'two', False, 4)
print(tuple_two)

print(tuple_two * 2)  # Duplicate the tuple
print(tuple_one + tuple_two)  # merge two tuples

# No valid, tuples are immutable
# tuple_two[0] = True


# Dictionaries

dict = {
    "name": 'Name',
    "number": 4,
    "bool": True,
    "list": [1, 2, 3, 4],
    4: "four",
    True: 67
}
print(dict)
print(dict[4])
print(dict[True])
print(dict.keys())
print(dict.values())

for i in dict.values():
    print(i)
