"""
list comprehention:
we can achive same result of map, filter using this.
basic syntax of this is:
[expression for item in items]

"""

items = [
    ('Product1', 10),
    ('Product2', 5),
    ('Product3', 30),
]

# example-1 (apply list comprehension)
prices = [item[1] for item in items]

print("After applying list comprehension \n", prices)

# example-2 (to filter the list)
filtered_prices = [item[1] for item in items if item[1] >= 10]
print("the filtered function applied in list comprehension is \n", filtered_prices)

# example-3 (find the max values among the filtered list)
filtered_prices = max([item[1] for item in items if item[1] >= 10])
print("the maximum values in the filtered list is \n", filtered_prices)