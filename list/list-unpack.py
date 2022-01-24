"""
list unpacking:
instead of assigning values of a list, we can 
directly apply unpacking approach which is 
supported by python
"""
# example -1
books = ['science', 'physics', 'chemistry']
category_first, category_second, category_third = books

print(category_first)
print(category_second)
print(category_third)

# example-2
cat_1, *others = books
print('many books are: ', others)