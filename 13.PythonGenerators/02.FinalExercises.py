def separator():
    print('-' * 20)


# Problem 1
# Create a generator that generates the squares of numbers up to some number N.

def gensquares(n):
    for x in range(n):
        yield x ** 2


for x in gensquares(10):
    print(x)

# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81

separator()

# Problem 2
# Create a generator that yields "n" random numbers between a low and high number (that are inputs).
# Note: Use the random library. For example:

import random

random.randint(1, 10)


def rand_num(low, high, n):
    for x in range(n):
        yield random.randint(low, high)


for num in rand_num(1, 10, 12):
    print(num)

# 7
# 7
# 9
# 5
# 8
# 7
# 3
# 10
# 7
# 7
# 1
# 8

separator()

# Problem 3
# Use the iter() function to convert the string below into an iterator:

s = 'hello'
s_iter = iter(s)

print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))

# h
# e
# l
# l
# o

separator()

# Problem 4
# Explain a use case for a generator using a yield statement where you would not want to use a normal function with a return statement.

# When we want to iterate lists that takes up too much memory
