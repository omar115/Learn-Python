items = [
    ('Product1', 10),
    ('Product2', 20),
    ('Product3', 30),
]

# example-1 (get a list of numbers only)
prices=[]
for item in items:
    prices.append(item[1])

print('price after using loop ', prices)

# example-2 (use map to do that)
x = map(lambda item: item[1], items)    # will return a map object
final_result = list(map(lambda item: item[1], items))    # will return a list object


print('after using map the result is\n', final_result)