# Basic function


def my_function():
    print('Basic function was called')


# Function with arguments

def my_function_2(name, age, salary=0):
    print('Name is %s' % name)
    print('Age is %d' % age)
    print('Salary is %d' % salary)


# N number of arguments


def add(*numbers):
    my_sum = 0
    for i in numbers:
        my_sum = my_sum + i;
    return my_sum


print(add(1, 2, 3, 4, 5, 6, 7))


# Lambda functions


def my_fun(n):
    return lambda a: a * n


doubler = my_fun(2)

print(doubler(11))
