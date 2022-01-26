
def calculate(age):
    if age <= 0:
        raise ValueError
    else:
        print("AGE: ", age)

calculate(12)