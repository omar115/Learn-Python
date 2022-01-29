"""
variable message is defined under a function.
that is why it is called a local variable
under a function. If we want to access this 
outside it will raise an error.
local variable has short memory lifetime.
after executing the particular function, local 
variable will be handled by python interpreter
garbage collector.
but global variable has bigger span of lifetime.
*coding good practice is to use local variable.
"""

message = "a"
def greet():
    message = "b"
greet()
print(message)  # will print a