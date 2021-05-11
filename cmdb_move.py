import requests
import json

name = {'j/new_search_subjects?sort=U&range=0,10&tags=&start=20': '',
        '10.1.1.110:3001/v1/hwinventory': '{"ips":["10.202.200.114"]}',
        '/cmdb/v1/bandwidth-rate/conf': '',
        '/cmdb/v1/disk-rate/conf': '',
        '/cmdb/v1/idc/info': '',
        '/cmdb/v1/disk-type/info': '{ "idc": "东涌机房" }',
        '/cmdb/v1/memory/info': '{ "diskType": "云盘" }',
        '/cmdb/v1/biz-line/info': '{ "bizLine": "IM业务线" }',
        ' /cmdb/v1/app-info': '{ "service_id": 12345, "service_name": "车主监控服务" }',
        '/cmdb/v1/app-relate-user/info': '{}',
        '/cmdb/v1/app/man': '{ "appName": "车主监控服务" }',
        '/cmdb/v1/app-db/info': '{ "appId": "xxxxx", "appName": "车主监控服务" }',
        '/cmdb/v1/app-ex/info': '{ "app_list": [ { "ip": "xxx", "app": "xxxx" }, { "ip": "xxx", "app": "xxxx" } ] }',
        '/cmdb/v1/app/tree': '{ "appName": "obd-server-proto-g" }',
        '/cmdb/v1/app-owner/info': '{ "appName": "obd-server-proto-g" }'
        }


class cmdb_move(object):

    def __init__(self, name):
        # self.url = 'http://10.1.1.110:3001/v1/hwinventory'
        self.name = name
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        }
        # self.real_url = self.url + self.name

    def req_get(self):
        self.url = 'https://movie.douban.com/'
        self.real_url = self.url + self.name
        try:
            self.respone = requests.get(url=self.real_url, headers=self.headers)
            data = self.respone.text
            data = json.loads(data)
        except:
            print('不是json数据')
        else:
            data_json = json.dumps(data, indent=4, ensure_ascii=False, sort_keys=False, separators=(',', ':'))
            if data['data'] == '00000':
                print('接口正常')
            else:
                print(self.real_url)
                print(data_json)

    def req_post(self, json):
        self.url = 'http://10.1.1.110:3001/v1/hwinventory'
        self.real_url = self.url + self.name
        try:
            self.respone = requests.post(url=self.real_url, data=json, headers=self.headers)
            data = self.respone.text
            data = json.loads(data)
        except:
            print('不是json数据')
        else:
            data_json = json.dumps(data, indent=4, ensure_ascii=False, sort_keys=False, separators=(',', ':'))
            if data['data'] == '00000':
                print('接口正常')
            else:
                print(self.real_url)
                print(data_json)


if __name__ == '__main__':
    for key, value in name.items():
        if value is '':
            resp = cmdb_move(key)
            resp.req_get()

        else:
            resp = cmdb_move(key)
            value_json = json.dumps(value)
            resp.req_post(json.dumps(value_json))
