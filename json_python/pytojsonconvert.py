#convert python different type of data to json data

import json

print(json.dumps({"name": "John", "age": 30}))  #dictionary to json object
print(json.dumps(["apple", "bananas"])) #list to json to array
print(json.dumps(("apple", "bananas"))) #tuple to json array
print(json.dumps("hello"))  #string to json string
print(json.dumps(42))   #integer to json number
print(json.dumps(31.76))    #float to json number
print(json.dumps(True))     #boolean to json 
print(json.dumps(False))    #boolean to json
print(json.dumps(None))     #none to json   null
