"""
the else statement will only work when
the break statement will never be executed.

"""

success = False
for number in range(3):
    print("Attempt")
    if success:
        print("Succeeded")
        break

else:
    print("Attempted 3 times but failed")