try:
    age = int(input("AGE: "))
    xfactor = 10 / age

# example-1
except ValueError as e:
    print("You did not enter a valid age\n", e)

# example-2
except Exception as e:
    print("Some other bugs\n", e)

# can be apply similar to for else loop
# will only execute if try block works

else:
    print("execution continues..")