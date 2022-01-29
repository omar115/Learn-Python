"""
annonynimous function.
"""

items = ["book1", "book2", "book3"]
items = [
    ('book1', 10),
    ('book2', 20),
    ('book3', 30)
]
items.sort(key=lambda item:item[1])

print(items)