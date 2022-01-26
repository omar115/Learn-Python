try:
    age = int(input("AGE: "))

except ValueError as e:
    print("You did not enter a valid age\n", e)

# can be apply similar to for else loop
# will only execute if try block works

else:
    print("execution continues..")