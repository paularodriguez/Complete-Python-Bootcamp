# Generators allow us to generate a sequence of values over time

# For example, the range() function doesn't produce a list in memory for all the values from start to stop
# Instead, it just keeps track of the last number and the step size, to provide a flow of numbers

# Using normal function: we store all cubes in memory
def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x ** 3)
    return result


for x in create_cubes(10):
    print(x)


# New function version to avoid store cubes in memory using yield
# Yields tracks the last used number
def create_cubes(n):
    for x in range(n):
        yield x ** 3


# This version is more efficient than previous one
for x in create_cubes(10):
    print(x)

# To get the list of cubes:
cubes = list(create_cubes(10))
print(cubes)


# Another example: Fibonacci numbers
def gen_fibonacci(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


for number in gen_fibonacci(10):
    print(number)


# Another example

def simple_gen():
    for x in range(3):
        yield x


for x in simple_gen():
    print(x)

g = simple_gen()

# <generator object simple_gen at 0x1063fe3d0>
print(g)
# 0
print(next(g))
# 1
print(next(g))
# 2
print(next(g))
# Error: range is up to 3: all values have been yielded
# print(next(g))
# When we use the generator in a for loop, the for loop automatically catches the error and stops


# ITER function: Allow us to automatically iterate through a normal object that you may not expect
s = 'hello'
for letter in s:
    print(letter)

# hello string is not iterable using next() function
# print(next(s)) -> ERROR

# solution
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
