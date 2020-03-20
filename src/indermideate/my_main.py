# Suppose this is foo.py.

import math
import my_random

print("before functionA")


def functionA():
    print("Function A")


print("before functionB")


def functionB():
    print("Function B {}".format(math.sqrt(100)))


print("before __name__ guard")

print(__name__);
if __name__ == '__main__':
    functionA()
    functionB()
print("after __name__ guard")
