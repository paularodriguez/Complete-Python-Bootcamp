# one.py

# Built in variable
# __name__

# if we run: python one.py python does the following:
# __name__ = "__main__"

# Example

def func():
    print("FUNC() IN ONE.PY")


print("TOP LEVEL IN ONE.PY")

if __name__ == '__main__':
    print('ONE.PY is being run directly!')
else:
    print("ONE.PY has been imported!")

# When we use the __name__ variable is to execute all functions that have been defined previously

if __name__ == '__main__':
    # RUN THE SCRIPT
    func()
    pass
