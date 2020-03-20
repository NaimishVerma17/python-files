import random


def my_generator():
    for i in range(6):
        yield random.randint(1, 20)


res = my_generator()
for r in res:
    print(r)
print(res)
