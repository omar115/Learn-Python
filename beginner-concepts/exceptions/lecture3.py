"""
finally clause will always executed,
no matter you have exception or not.
the approach is useful for closing db
or network connection.
"""

try:
    file = open("lecture2.py")
    age = int(input("AGE: "))
    xfactor = 10 / age
    file.close()

# example-2
except Exception as e:
    print("Some other bugs\n", e)

else:
    print("execution continues..")

finally:
    file.close()