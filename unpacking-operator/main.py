
# example-1
numbers = [1, 2, 3]
print(*numbers)

# example-2
values = list(range(5))
print(values)

# example-3 (unpack)
values = [*range(5)]
print(values)

# example-4 (unpack)
values = [*range(5), *'Hello']
print(values)

# example-5 (unpack dict)
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
print("dict unpack: ", combined)
