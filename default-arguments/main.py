"""
we can use default argument in defining our
function.
"""

def increment(number, by=1):
    return number + by

# example-1
print(increment(2))

# example-2
print(increment(2, 5))