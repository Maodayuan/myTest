# import requests
# import json
#
# date = {"ips": ["10.202.201.106"]}
# r = requests.post('http://10.1.1.110:3001/v1/hwinventory', json=date)
# q = r.text
# j = json.loads(q)
# print(type(j))
# cpu = j['data']['ipdata'][0]['cpu']
# cpu_json = json.dumps(cpu, indent=4, ensure_ascii=False, sort_keys=False, separators=(',', ':'))
# print('CPU:{}'.format(cpu_json))
#
# dimm = j['data']['ipdata'][0]['dimm']
# dimm_json = json.dumps(dimm, indent=4, ensure_ascii=False, sort_keys=False, separators=(',', ':'))
# print('内存:{}'.format(dimm_json))
#
# disk = j['data']['ipdata'][0]['disk']
# disk_json = json.dumps(disk, indent=4, ensure_ascii=False, sort_keys=False, separators=(',', ':'))
# print('磁盘:{}'.format(disk_json))
#
# net = j['data']['ipdata'][0]['net']
# net_json = json.dumps(net, indent=4, ensure_ascii=False, sort_keys=False, separators=(',', ':'))
# print('网卡:{}'.format(net_json))
#
# for subport in net:
#     subport_json = json.dumps(subport, indent=4, ensure_ascii=False, sort_keys=False, separators=(',', ':'))
#     print('网口:{}'.format(subport_json))
#
# physical_info = j['data']['ipdata'][0]['physical_info']
# physical_info_json = json.dumps(physical_info, indent=4, ensure_ascii=False, sort_keys=False, separators=(',', ':'))
# print('硬件服务:{}'.format(physical_info_json))

import requests
import json

date = {"ips": ["10.202.201.106"]}
r = requests.post('http://10.1.1.110:3001/v1/hwinventory', json=date)
j = json.loads(r.text)
items = ['cpu', 'dimm', 'disk', 'net', 'physical_info']

for item in items:
    data_non = j['data']['ipdata'][0][item]
    if isinstance(data_non, list):
        data = data_non
    else:
        data = []
        data.append(data_non)
    data_json = json.dumps(data, indent=4, ensure_ascii=False, sort_keys=False, separators=(',', ':'))
    print('数量-{}'.format(len(data)))
    print('{}:{}'.format(item, data_json))


for subport in j['data']['ipdata'][0]['net']:

    subport_data = subport['subPorts']
    if isinstance(subport_data, list):
        data = subport_data
    else:
        data = []
        data.append(subport_data)
    data_json = json.dumps(data, indent=4, ensure_ascii=False, sort_keys=False, separators=(',', ':'))
    print('数量-{}'.format(len(data)))
    print('subPorts:{}'.format(data_json))
