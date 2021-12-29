import traceback

p = (4, 5)
x,y = p

print('After unpacking the tuple the x val >> ',x,'\nthe y value >> ',y)
# print(y)

# example-2
data = ['ACME',50,91.1, (2012,12,21)]
name,v1,v2,date=data
print('The date is >> ',date)

# example-3
# possible error message
p = (4,5)
try:
    x,y,z=p
except:
    print(traceback.format_exc())


# example-4
# using * expression

record = ('Dave','dave@email.com','773-555-883','888-999-000-111')
name, email, *phone_numbers = record

print('all the phone numbers are: ', phone_numbers)

# example-5

items = [1, 2, 10, 20, 8, 7, 5]
head, *tails = items
print('the tails part are>> ',tails)
