"""
generator object is iterable. you do not need to store
values in memory, instead you generate a new value
in each iteration
in situation of working with really large dataset,
we use generator expression as it is memory efficient
"""
from sys import getsizeof

values = (x * 2 for x in range(5))
print(values)
for x in values:
    print(x)

# example-2 (get size of generator)
values = (x * 2 for x in range(1000000))
print("gen: ", getsizeof(values))

# compare with list
values = [x * 2 for x in range(1000000)]
print("list: ", getsizeof(values))