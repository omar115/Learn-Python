"""
using * sign we can send multiple values.
if we want to print it, it will return a tuple,
which can not be editable later.

"""

def multiply(*numbers):
    return numbers

print(multiply(2, 3, 4, 5))