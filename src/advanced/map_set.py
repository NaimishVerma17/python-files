list = (1, 2, 3, 4, 5, 6)


def generate_square(num):
    return num * num


res = map(generate_square, list)

res = set(res)

# Not necessarily in the same order as the original list
print(res)
