# class Clang:
#     def __init__(self,name):
#         self.name = name
#     def setname(self,name):
#         self.name = name
#     def getname(self):
#         return self.name
#     def delname(self):
#         self.name='xxx'
# clang=Clang('python')
# print(clang.getname())
# clang.setname('dd')
# print(clang.getname())
# clang.delname()
# print(clang.getname())
# print('hello world')
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com/')
# driver.quit()
# from selenium import webdriver
# path = '/usr/local/bin/chromedriver'
# # path = '/Users/maodayuan/Desktop/mytest/chromedriver'
# driver = webdriver.Chrome(executable_path=path)
# driver.get('http://www.baidu.com')

#
# import json
#
# data = [
#     {
#         "a": {
#             "identity": 4,
#             "labels": [
#                 "Model"
#             ],
#             "properties": {
#                 "uid": "ip",
#                 "editor": "xiangchao",
#                 "creator": "xiangchao",
#                 "createTime": 1617098678,
#                 "name": "IP池",
#                 "updateTime": 1617098678,
#                 "iconUrl": "",
#                 "uuid": "59180e14-c64d-4a8c-9ab7-68a8f165248c"
#             }
#         }
#     },
#     {
#         "a": {
#             "identity": 5,
#             "labels": [
#                 "Model"
#             ],
#             "properties": {
#                 "uid": "warehouse",
#                 "editor": "xiangchao",
#                 "creator": "xiangchao",
#                 "createTime": 1617098713,
#                 "name": "仓库",
#                 "updateTime": 1617098713,
#                 "iconUrl": "",
#                 "uuid": "25e3b58b-3a7f-4b40-b493-803dad50d231"
#             }
#         }
#     },
#     {
#         "a": {
#             "identity": 7,
#             "labels": [
#                 "Model"
#             ],
#             "properties": {
#                 "uid": "memory",
#                 "editor": "xiangchao",
#                 "creator": "xiangchao",
#                 "createTime": 1617098739,
#                 "name": "存储器",
#                 "updateTime": 1617098739,
#                 "iconUrl": "",
#                 "uuid": "bb6ee2ce-88df-4e28-b430-910db52ba301"
#             }
#         }
#     },
#     {
#         "a": {
#             "identity": 9,
#             "labels": [
#                 "Model"
#             ],
#             "properties": {
#                 "uid": "order",
#                 "editor": "xiangchao",
#                 "creator": "xiangchao",
#                 "createTime": 1617098783,
#                 "name": "订单",
#                 "updateTime": 1617098783,
#                 "iconUrl": "",
#                 "uuid": "5793cf8d-6374-4f2a-836a-f1fbdd6b4709"
#             }
#         }
#     },
#     {
#         "a": {
#             "identity": 10,
#             "labels": [
#                 "Model"
#             ],
#             "properties": {
#                 "uid": "contract",
#                 "editor": "xiangchao",
#                 "creator": "xiangchao",
#                 "createTime": 1617098808,
#                 "name": "合同",
#                 "updateTime": 1617098808,
#                 "iconUrl": "",
#                 "uuid": "1111e5ec-635f-4abc-8e26-9e6fdb6114e2"
#             }
#         }
#     },
#     {
#         "a": {
#             "identity": 11,
#             "labels": [
#                 "Model"
#             ],
#             "properties": {
#                 "uid": "room",
#                 "editor": "xiangchao",
#                 "creator": "xiangchao",
#                 "createTime": 1617098825,
#                 "name": "机房",
#                 "updateTime": 1617098825,
#                 "iconUrl": "",
#                 "uuid": "1f260e4e-7175-42ba-b185-d9f392327db5"
#             }
#         }
#     },
#     {
#         "a": {
#             "identity": 13,
#             "labels": [
#                 "Model"
#             ],
#             "properties": {
#                 "uid": "cabinet",
#                 "editor": "xiangchao",
#                 "creator": "xiangchao",
#                 "createTime": 1617098850,
#                 "name": "机柜",
#                 "updateTime": 1617098850,
#                 "iconUrl": "",
#                 "uuid": "5b0d130d-090b-4224-b9fb-0dfe083f4ecd"
#             }
#         }
#     },
#     {
#         "a": {
#             "identity": 14,
#             "labels": [
#                 "Model"
#             ],
#             "properties": {
#                 "uid": "link",
#                 "editor": "xiangchao",
#                 "creator": "xiangchao",
#                 "createTime": 1617098883,
#                 "name": "链路",
#                 "updateTime": 1617098883,
#                 "iconUrl": "",
#                 "uuid": "4a64daf6-9674-4b1e-8e2d-b1a53112da23"
#             }
#         }
#     },
#     {
#         "a": {
#             "identity": 17,
#             "labels": [
#                 "Model"
#             ],
#             "properties": {
#                 "uid": "equipment",
#                 "editor": "xiangchao",
#                 "creator": "xiangchao",
#                 "createTime": 1617098912,
#                 "name": "网络设备",
#                 "updateTime": 1617098912,
#                 "iconUrl": "",
#                 "uuid": "601b3ae0-6f73-4cf9-ba2f-4a75e9b2f89b"
#             }
#         }
#     },
#     {
#         "a": {
#             "identity": 19,
#             "labels": [
#                 "Model"
#             ],
#             "properties": {
#                 "uid": "physical_server",
#                 "editor": "xiangchao",
#                 "creator": "xiangchao",
#                 "createTime": 1617098975,
#                 "name": "物理服务器",
#                 "updateTime": 1617098975,
#                 "iconUrl": "",
#                 "uuid": "b32197c0-2df5-4fc1-a6e9-1fe75d1d793a"
#             }
#         }
#     },
#     {
#         "a": {
#             "identity": 22,
#             "labels": [
#                 "Model"
#             ],
#             "properties": {
#                 "uid": "cpu",
#                 "editor": "xiangchao",
#                 "creator": "xiangchao",
#                 "createTime": 1617098994,
#                 "name": "CPU",
#                 "updateTime": 1617098994,
#                 "iconUrl": "",
#                 "uuid": "d85e3102-fb9d-41b3-a6cb-74fd71ab0695"
#             }
#         }
#     },
#     {
#         "a": {
#             "identity": 26,
#             "labels": [
#                 "Model"
#             ],
#             "properties": {
#                 "uid": "ram",
#                 "editor": "xiangchao",
#                 "creator": "xiangchao",
#                 "createTime": 1617099155,
#                 "name": "内存",
#                 "updateTime": 1617099155,
#                 "iconUrl": "",
#                 "uuid": "65e21679-7e8f-46ca-8a43-e8b87df9da7a"
#             }
#         }
#     },
#     {
#         "a": {
#             "identity": 27,
#             "labels": [
#                 "Model"
#             ],
#             "properties": {
#                 "uid": "network_card",
#                 "editor": "xiangchao",
#                 "creator": "xiangchao",
#                 "createTime": 1617099182,
#                 "name": "网卡",
#                 "updateTime": 1617099182,
#                 "iconUrl": "",
#                 "uuid": "d73b6781-1986-47f2-94b4-64dea8e27023"
#             }
#         }
#     },
#     {
#         "a": {
#             "identity": 28,
#             "labels": [
#                 "Model"
#             ],
#             "properties": {
#                 "uid": "network_port",
#                 "editor": "xiangchao",
#                 "creator": "xiangchao",
#                 "createTime": 1617099199,
#                 "name": "网口",
#                 "updateTime": 1617099199,
#                 "iconUrl": "",
#                 "uuid": "0ac9d213-30ec-48ad-b200-3d414c7a3f82"
#             }
#         }
#     },
#     {
#         "a": {
#             "identity": 30,
#             "labels": [
#                 "Model"
#             ],
#             "properties": {
#                 "uid": "physical_disk",
#                 "editor": "xiangchao",
#                 "creator": "xiangchao",
#                 "createTime": 1617099218,
#                 "name": "物理磁盘",
#                 "updateTime": 1617099218,
#                 "iconUrl": "",
#                 "uuid": "eae388e8-e315-43b0-98e7-405fc13840fa"
#             }
#         }
#     },
#     {
#         "a": {
#             "identity": 34,
#             "labels": [
#                 "Model"
#             ],
#             "properties": {
#                 "uid": "virtual_disk",
#                 "editor": "xiangchao",
#                 "creator": "xiangchao",
#                 "createTime": 1617099413,
#                 "name": "虚拟磁盘（阵列）",
#                 "updateTime": 1617099413,
#                 "iconUrl": "",
#                 "uuid": "c8c132d9-19b9-4795-a968-1bc303276c1a"
#             }
#         }
#     },
#     {
#         "a": {
#             "identity": 36,
#             "labels": [
#                 "Model"
#             ],
#             "properties": {
#                 "uid": "system",
#                 "editor": "xiangchao",
#                 "creator": "xiangchao",
#                 "createTime": 1617099443,
#                 "name": "操作系统",
#                 "updateTime": 1617099443,
#                 "iconUrl": "",
#                 "uuid": "3dd2e9ec-6678-425f-b077-976297f17020"
#             }
#         }
#     },
#     {
#         "a": {
#             "identity": 235,
#             "labels": [
#                 "Model"
#             ],
#             "properties": {
#                 "editor": "xiangchao",
#                 "uid": "maintenance_record",
#                 "creator": "xiangchao",
#                 "createTime": 1617333249,
#                 "name": "硬件维修记录",
#                 "updateTime": 1617344966,
#                 "iconUrl": "",
#                 "uuid": "55f6b986-9946-4a11-a250-1c311964bcce"
#             }
#         }
#     },
#     {
#         "a": {
#             "identity": 238,
#             "labels": [
#                 "Model"
#             ],
#             "properties": {
#                 "uid": "change_record",
#                 "editor": "xiangchao",
#                 "creator": "xiangchao",
#                 "createTime": 1617344511,
#                 "name": "硬件变动记录",
#                 "updateTime": 1617344974,
#                 "iconUrl": "",
#                 "uuid": "5cf1158d-9247-43a7-88f1-5936e9f319b0"
#             }
#         }
#     }
# ]
#
# data_json = json.dumps(data, indent=4, ensure_ascii=False, sort_keys=False, separators=(',', ':'))
#
# print(type(data_json))
# print(data_json)
#
# import unittest
#
#
# class TestBdd(unittest.TestCase):
#
#     def setUp(self) -> None:
#         print("test TestBdd")
#
#     def test_ccc(self):
#         print("test ccc")
#
#     def test_aaa(self):
#         print("test aaa")
#
#
# class TestAdd(unittest.TestCase):
#
#     def setUp(self) -> None:
#         print("test TestAdd:")
#
#     def test_bbb(self):
#         print("test bbb")
#
#
# if __name__ == "__main__":
#     suite = unittest.TestSuite()
#     suite.addTest(TestBdd('test_aaa'))
#     suite.addTest(TestBdd("test_ccc"))
#     suite.addTest(TestAdd("test_bbb"))
#
#     runner = unittest.TextTestRunner()
#     runner.run(suite)
# import unittest
#
#
# class MyTest(unittest.TestCase):
#
#     @unittest.skip('直接跳过测试')
#     def test_skip(self):
#         print("test aaa")
#
#     @unittest.skipIf(3 > 2, '当条件为真时跳过测试')
#     def test_skip_if(self):
#         print("test bbb")
#
#     @unittest.skipUnless(3 > 2, '当条件为真时执行测试')
#     def test_skip_unless(self):
#         print('test ccc')
#
#     @unittest.expectedFailure
#     def test_expected_failure(self):
#         self.assertEqual(2, 3)
#
#
# if __name__ == "__main__":
#     unittest.main()
# import unittest
#
#
# def setUpModule():
#     print("test module start >>>>>>>>>>>>>>")
#
#
# def tearDownModule():
#     print("test module end >>>>>>>>>")
#
#
# # 113
# class MyTest(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls) -> None:
#         print('test class start =====>')
#
#     @classmethod
#     def tearDownClass(cls) -> None:
#         print("test class end =====>")
#
#     def setUp(self) -> None:
#         print('test case start -->')
#
#     def tearDown(self) -> None:
#         print('test case end ---->')
#
#     def test_case1(self):
#         print('test case1')
#
#     def test_case2(self):
#         print('test case2')


# if __name__ == "__main__":
#     unittest.main()
#
# import requests
# from requests import Request, Session
# import re

# url = 'http://httpbin.org/post'
# data = {'name': 'tom'}
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
#     }
# s = Session()
# req = Request('POST', url, data=data, headers=headers)
# prepped = s.prepare_request(req)
# r = s.send(prepped)
# print(r.text)

# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^He.*?(\d+).*Demo$', content)
# print(result)
# print(result.group())
# print(result.group(1))
# print(result.span())


# from urllib.parse import urlencode
# import requests
# base_url = 'https://m.weibo.cn/api/container/getIndex?'
#
# headers = {
#     'Host': 'm.weibo.cn',
#     'Referer': 'https://m.weibo.cn/u/2830678474',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
#     'X-Requested-With': 'XMLHttpRequest',
# }
#
# requests.get()
html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
print(soup.p.descendants)
for i, child in enumerate(soup.p.descendants):
    print(i, child)
