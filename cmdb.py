import requests
import json

date = {"ips": ["10.202.201.106"]}
r = requests.post('http://10.1.1.110:3001/v1/hwinventory', json=date)
q = r.text
j = json.loads(q)
print(type(j))
cpu = j['data']['ipdata'][0]['cpu']
cpu_json = json.dumps(cpu, indent=4, ensure_ascii=False, sort_keys=False, separators=(',', ':'))
# print('CPU:{}'.format(cpu_json))

dimm = j['data']['ipdata'][0]['dimm']
dimm_json = json.dumps(dimm, indent=4, ensure_ascii=False, sort_keys=False, separators=(',', ':'))
# print('内存:{}'.format(dimm_json))

disk = j['data']['ipdata'][0]['disk']
disk_json = json.dumps(disk, indent=4, ensure_ascii=False, sort_keys=False, separators=(',', ':'))
# print('磁盘:{}'.format(disk_json))

net = j['data']['ipdata'][0]['net']
net_json = json.dumps(net, indent=4, ensure_ascii=False, sort_keys=False, separators=(',', ':'))
# print('网卡:{}'.format(net_json))

subPorts = j['data']['ipdata'][0]['net'][0]['subPorts']
subPorts_json = json.dumps(subPorts, indent=4, ensure_ascii=False, sort_keys=False, separators=(',', ':'))
print('网卡:{}'.format(subPorts_json))

physical_info = j['data']['ipdata'][0]['physical_info']
physical_info_json = json.dumps(physical_info, indent=4, ensure_ascii=False, sort_keys=False, separators=(',', ':'))
print('硬件服务:{}'.format(physical_info_json))
