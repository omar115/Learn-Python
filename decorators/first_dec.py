'''
source: Datacamp
A decorator is a design pattern in python allows the user to add new functionality to an existing
object without modifying its structure.

'''

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


# a function can be passed through another function

def fun_one(number):
    return number + 1

def fun_call_fun_one(function):
    add_number = 5
    return function(add_number)

print(fun_call_fun_one(fun_one))


# now use the decorator to make it simple

def uppercase_decorator(function):
    def wrapper():
        func = function
        make_uppercase = func.upper()

        return make_uppercase
    return wrapper

@uppercase_decorator
def say_hi():
    return 'hello there'

print(say_hi)   # return the location 


# @uppercase_decorator
# def say_hi():
#     return 'hello man'

# print(say_hi())
