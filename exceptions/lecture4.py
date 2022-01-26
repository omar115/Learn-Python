"""
if we use with statement, we do not need
finally anymore for this scenario. but after
executing with statement, python will automically
called to close everthing. so, file.close()
will be called by with statement automically.
"""

try:
    with open("lecture2.py") as file:
        print("File opened")
        
    # file = open("lecture2.py")
    age = int(input("AGE: "))
    xfactor = 10 / age
    file.close()

# example-2
except Exception as e:
    print("Some other bugs\n", e)

else:
    print("execution continues..")
