
"""
the range function returns an range object which is
iterable means we can iterate it.

String object will also iterable.
"""

# example-1
print(type(range(5)))

# example 2 (iterate over string)
for x in "Python":
    print(x)

# example-3 (iterate over list)
for x in [1, 2, 3]:
    print(x)