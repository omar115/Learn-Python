import json

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann","Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x))

#formatting the results with indent
print(json.dumps(x, indent=2))

#sort_keys to used to combine the alphabetical orders

print(json.dumps(x, indent=2, sort_keys=True))