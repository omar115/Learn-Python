phone_book = {
    "name": "Hasan",
    "number": 12764
}

print(phone_book)

point = dict(x=1, y=2)
print(point["x"])
point["x"] = 10
print(point["x"])

# example-1 (if no item exist it will return None)
print(point.get("a"))

# example-2 (you can define the return value)
print(point.get("a", 0))

# del item
del point["x"]
print("After deleting the item\n", point)

# loop over dict
for key in point:
    print(key, point[key])

# loop over dict (example-2)
for x in point.items():
    print(x)