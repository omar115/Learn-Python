items = [
    ('Product1', 10),
    ('Product2', 5),
    ('Product3', 30),
]

# example-1 (use built in filter function)
x = filter(lambda item: item[1] >= 10, items)   # will return filter object
final_result = x = list(filter(lambda item: item[1] >= 10, items))   # will return list object

print("filtered result is \n", final_result)