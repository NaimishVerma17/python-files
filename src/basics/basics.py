# Basic hello world
print('Hello world')

# Print in two lines
print('Line 1 \n Line 2')

# input for printing each character
limit = input('Enter the word.')

for i in limit:
    print(i)

# Variables
variable_integer = 10
variable_decimal = 10.9
variable_string = 'Some random string'
variable_boolean = False

var_1, var_2 = 'Python', 3

# String formatting
result = 'I am learning {0} version {1:.2F}'

print(result.format(var_1, var_2))
