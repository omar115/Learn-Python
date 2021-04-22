import json

#create simple json file
# x = '{"name":"omar","age":25,"city":"Dhaka"}'

# #parsing
# data = json.loads(x)
# print(data)
# print(type(data))

# print(data['age'])


#convert python to json

x= {
    'name':'XX',
    'age':34,
    'city':'YY'
}

print('the dictionary is ',x)

#convert into json

data = json.dumps(x)

print('nwo the converted json data is ',data)