"""
the ** sign will take multiple arguments,
using this sign we can pass multiple key value
pairs and python will automically package them
into a dictionary.
"""

def save_user(**user):
    # example-1 (print the dictionary)
    print(user)

    # example-2 (print the user name)
    print(user["name"])

    # example-3 (print the user name and city name)
    print(user["name"], user["city"])

save_user(id=1, name="Amit", age=22, city="Dhaka")