import requests
import json

date = {"ips": ["10.202.201.106"]}
r = requests.post('http://10.1.1.110:3001/v1/hwinventory', json=date)
q = r.text
j = json.loads(q)
print(j)
print(type(j))
print(j['code'])
message = json.dumps(j, indent=4, ensure_ascii=False, sort_keys=False, separators=(',', ':'))
print(message)
