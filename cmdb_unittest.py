import unittest
import requests
import json

# name = {'/cmdb/v1/bandwidth-rate/conf': '', 'get_disk_rate': '/cmdb/v1/disk-rate/conf',
#         'get_idcinfolist': '/cmdb/v1/idc/info', 'get_disktypeinfo': '/cmdb/v1/disk-type/info'
#         }
name = {'douban': 'j/new_search_subjects?sort=U&range=0,10&tags=&start=20'}


class TestCmdb(unittest.TestCase):
    def setUp(self) -> None:
        print('test cmdb:')

    def test_cmdb_move(self):
        url = 'https://movie.douban.com/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        }
        respone = requests.get(url=url, headers=headers)
        data = respone.text
        data = json.loads(data)
        data_json = json.dumps(data, indent=4, ensure_ascii=False, sort_keys=False, separators=(',', ':'))
        print(data_json[data])
        print(data_json[data])
        # self.assertEqual()

        url = 'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start=20'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        }
        respone = requests.get(url=url, headers=headers)
        data = respone.text
        data = json.loads(data)
        data_json = json.dumps(data, indent=4, ensure_ascii=False, sort_keys=False, separators=(',', ':'))
        # print(data_json)
        print(data['data'])
        # print(data[data])


if __name__ == '__main__':
    unittest.main()
