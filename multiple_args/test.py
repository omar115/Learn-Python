def sum(*args):
    result = ''
    for x in args:
        result += str(x)
    return result
    # return a+b+c+d

print(sum(1,2,3,4, ' Hello? ', 3.14, ' How are you?'))