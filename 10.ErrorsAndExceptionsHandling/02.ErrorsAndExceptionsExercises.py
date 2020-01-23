# Problem 1
# Handle the exception thrown by the code below by using try and except blocks.

try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except TypeError:
    print("Value is not an integer")

# Problem 2
# Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'

x = 5
y = 0

try:
    z = x / y
except ZeroDivisionError:
    print("Division by zero!!")
finally:
    print("All Done")


# Problem 3
# Write a function that asks for an integer and prints the square of it.
# Use a while loop with a try, except, else block to account for incorrect inputs.

# Input an integer: null
# An error occurred! Please try again!
# Input an integer: 2
# Thank you, your number squared is:  4

def ask():
    while True:
        try:
            value = int(input("Input an integer:"))
        except:
            print("An error occurred! Please try again!")
        else:
            result = value ** 2
            print("Thank you, your number squared is: " + str(result))
            break


ask()
