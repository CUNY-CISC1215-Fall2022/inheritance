# This file demonstrates using exceptions to deal with error conditions
# inside of a function.

# Recursively compute the factorial of n.
def factorial(n):
    # Use the guardian pattern to catch bad input. In this case, we cannot compute
    # the factorial of a negative number.
    if n < 0:
        # If this code is triggered, the factorial() function immediately terminates.
        # The exception bubbles up to whoever called the function, forcing them to
        # either deal with it (with a try/except block)or ignore it (terminating the program)
        raise Exception("Factorial cannot be computed for numbers less than 0")

    if n == 0:
        return 1
    
    return n * factorial(n-1)

# This list contains several numbers we want to compute the factorial over.
# Note one of the numbers is negative!
numbers = [1, 2, 3, -10, 4, 5, 6]

# Iterate over the numbers and compute the factorial for all of them
for n in numbers:
    if n >= 0:
        # Because calling factorial() is potentially dangerous (i.e., it may raise an exception),
        # we wrap our call in a try/except block:
        try:
            print(f"Factorial of {n}: {factorial(n)}")
        except:
            # If factorial() raises an exception, control will immediately transfer here
            print(f"Cannot compute factorial for input {n}!")