import json

json_string = """
{
    "researcher": {
        "name": "John Wick",
        "species": "Meta Human",
        "Age":25,
        "relatives": [
            {
                "name": "Jane Doe",
                "species": "Meta Human - 2"
            }
        ]
    }
}
"""

data = json.loads(json_string)  #loading json data
print(data) #printting data
print('The type of json data in python is ',type(data))
print(type(data['researcher']))