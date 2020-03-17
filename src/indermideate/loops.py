# While loop

var1 = 1
while var1 <= 20:
    print('The value is: ', var1, end=';\n')
    if var1 >= 5:
        break
    var1 = var1 + 1

# For loop
for i in range(1, 10, 2):
    if i == 5:
        continue
    print('The value is: ', i, end=';\n')

for i in 'Python':
    print('The value is: ', i, end=';\n')

# Trick of else

var_list = [1, 2, 3, 4, 5, 6, 7, 8]
num = int(input('Enter the number'))

for i in var_list:
    if i == num:
        print('Match found!')
        break
else:
    print('Match not found!')

print('Outside loop')
