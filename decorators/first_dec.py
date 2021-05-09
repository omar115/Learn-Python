# normal function to illustrate basic activity of function
def plus_one(val1, val2):
    sum = val1 + val2
    return sum

print(plus_one(7,3))

# defining function inside another function
def plus_two(val1,val2):
    def add(val1):
        sum = val1+10
        return sum
    print(add(5))

plus_two(1,2)