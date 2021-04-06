import os
import json
with open('model.json','r') as f:
    file = f.read()
    print(type(file))

    j = json.loads(file)
    data_json = json.dumps(j, indent=4, ensure_ascii=False, sort_keys=False, separators=(',', ':'))

    print(type(j))
    print(data_json)