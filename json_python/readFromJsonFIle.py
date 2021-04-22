'''
here we will load a json file and manipulate data,
load method will load a file
loads method will load a string

dump method will convert the data to a json file

dumps method will convert the data to a json string

'''

import json

with open('./json_python/states.json') as f:
    data = json.load(f)
# print(data)

#how to print the data
for state in data['states']:
    # print(state['name'],state['abbreviation'])
    pass

#how to delete the data
for state in data['states']:
    del state['area_codes']


#how to write in a json file
with open('./json_python/new_states.json', 'w') as f:
    json.dump(data, f, indent=2)

