def sum(*args):
    result = 0
    for x in args:
        result += x
    return result
    # return a+b+c+d

print(sum(1,2,3,4))