# JSON = JavaScript Object Notation

import json

with open("data.json","r") as f:
    data = json.load(f)


#writing JSON to a file
with open("data2.json","w") as f:
    json.dump(data,f)