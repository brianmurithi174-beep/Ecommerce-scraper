import json

json_string = '''
{
    "students":[
        {
            "id":1,
            "Name":"Tim",
            "Age": 21,
            "full-time":true
        },
        {
            "id":2,
            "Name":"joe",
            "age":33,
            "full-time":false
        }

    ]
    }
'''
data = json.loads(json_string)
#print(data["students"])
data['test']=True
new_json = json.dumps(data, indent = 2)
print(new_json)
