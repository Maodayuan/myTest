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


import json

data = [
    {
        "a": {
            "identity": 4,
            "labels": [
                "Model"
            ],
            "properties": {
                "uid": "ip",
                "editor": "xiangchao",
                "creator": "xiangchao",
                "createTime": 1617098678,
                "name": "IP池",
                "updateTime": 1617098678,
                "iconUrl": "",
                "uuid": "59180e14-c64d-4a8c-9ab7-68a8f165248c"
            }
        }
    },
    {
        "a": {
            "identity": 5,
            "labels": [
                "Model"
            ],
            "properties": {
                "uid": "warehouse",
                "editor": "xiangchao",
                "creator": "xiangchao",
                "createTime": 1617098713,
                "name": "仓库",
                "updateTime": 1617098713,
                "iconUrl": "",
                "uuid": "25e3b58b-3a7f-4b40-b493-803dad50d231"
            }
        }
    },
    {
        "a": {
            "identity": 7,
            "labels": [
                "Model"
            ],
            "properties": {
                "uid": "memory",
                "editor": "xiangchao",
                "creator": "xiangchao",
                "createTime": 1617098739,
                "name": "存储器",
                "updateTime": 1617098739,
                "iconUrl": "",
                "uuid": "bb6ee2ce-88df-4e28-b430-910db52ba301"
            }
        }
    },
    {
        "a": {
            "identity": 9,
            "labels": [
                "Model"
            ],
            "properties": {
                "uid": "order",
                "editor": "xiangchao",
                "creator": "xiangchao",
                "createTime": 1617098783,
                "name": "订单",
                "updateTime": 1617098783,
                "iconUrl": "",
                "uuid": "5793cf8d-6374-4f2a-836a-f1fbdd6b4709"
            }
        }
    },
    {
        "a": {
            "identity": 10,
            "labels": [
                "Model"
            ],
            "properties": {
                "uid": "contract",
                "editor": "xiangchao",
                "creator": "xiangchao",
                "createTime": 1617098808,
                "name": "合同",
                "updateTime": 1617098808,
                "iconUrl": "",
                "uuid": "1111e5ec-635f-4abc-8e26-9e6fdb6114e2"
            }
        }
    },
    {
        "a": {
            "identity": 11,
            "labels": [
                "Model"
            ],
            "properties": {
                "uid": "room",
                "editor": "xiangchao",
                "creator": "xiangchao",
                "createTime": 1617098825,
                "name": "机房",
                "updateTime": 1617098825,
                "iconUrl": "",
                "uuid": "1f260e4e-7175-42ba-b185-d9f392327db5"
            }
        }
    },
    {
        "a": {
            "identity": 13,
            "labels": [
                "Model"
            ],
            "properties": {
                "uid": "cabinet",
                "editor": "xiangchao",
                "creator": "xiangchao",
                "createTime": 1617098850,
                "name": "机柜",
                "updateTime": 1617098850,
                "iconUrl": "",
                "uuid": "5b0d130d-090b-4224-b9fb-0dfe083f4ecd"
            }
        }
    },
    {
        "a": {
            "identity": 14,
            "labels": [
                "Model"
            ],
            "properties": {
                "uid": "link",
                "editor": "xiangchao",
                "creator": "xiangchao",
                "createTime": 1617098883,
                "name": "链路",
                "updateTime": 1617098883,
                "iconUrl": "",
                "uuid": "4a64daf6-9674-4b1e-8e2d-b1a53112da23"
            }
        }
    },
    {
        "a": {
            "identity": 17,
            "labels": [
                "Model"
            ],
            "properties": {
                "uid": "equipment",
                "editor": "xiangchao",
                "creator": "xiangchao",
                "createTime": 1617098912,
                "name": "网络设备",
                "updateTime": 1617098912,
                "iconUrl": "",
                "uuid": "601b3ae0-6f73-4cf9-ba2f-4a75e9b2f89b"
            }
        }
    },
    {
        "a": {
            "identity": 19,
            "labels": [
                "Model"
            ],
            "properties": {
                "uid": "physical_server",
                "editor": "xiangchao",
                "creator": "xiangchao",
                "createTime": 1617098975,
                "name": "物理服务器",
                "updateTime": 1617098975,
                "iconUrl": "",
                "uuid": "b32197c0-2df5-4fc1-a6e9-1fe75d1d793a"
            }
        }
    },
    {
        "a": {
            "identity": 22,
            "labels": [
                "Model"
            ],
            "properties": {
                "uid": "cpu",
                "editor": "xiangchao",
                "creator": "xiangchao",
                "createTime": 1617098994,
                "name": "CPU",
                "updateTime": 1617098994,
                "iconUrl": "",
                "uuid": "d85e3102-fb9d-41b3-a6cb-74fd71ab0695"
            }
        }
    },
    {
        "a": {
            "identity": 26,
            "labels": [
                "Model"
            ],
            "properties": {
                "uid": "ram",
                "editor": "xiangchao",
                "creator": "xiangchao",
                "createTime": 1617099155,
                "name": "内存",
                "updateTime": 1617099155,
                "iconUrl": "",
                "uuid": "65e21679-7e8f-46ca-8a43-e8b87df9da7a"
            }
        }
    },
    {
        "a": {
            "identity": 27,
            "labels": [
                "Model"
            ],
            "properties": {
                "uid": "network_card",
                "editor": "xiangchao",
                "creator": "xiangchao",
                "createTime": 1617099182,
                "name": "网卡",
                "updateTime": 1617099182,
                "iconUrl": "",
                "uuid": "d73b6781-1986-47f2-94b4-64dea8e27023"
            }
        }
    },
    {
        "a": {
            "identity": 28,
            "labels": [
                "Model"
            ],
            "properties": {
                "uid": "network_port",
                "editor": "xiangchao",
                "creator": "xiangchao",
                "createTime": 1617099199,
                "name": "网口",
                "updateTime": 1617099199,
                "iconUrl": "",
                "uuid": "0ac9d213-30ec-48ad-b200-3d414c7a3f82"
            }
        }
    },
    {
        "a": {
            "identity": 30,
            "labels": [
                "Model"
            ],
            "properties": {
                "uid": "physical_disk",
                "editor": "xiangchao",
                "creator": "xiangchao",
                "createTime": 1617099218,
                "name": "物理磁盘",
                "updateTime": 1617099218,
                "iconUrl": "",
                "uuid": "eae388e8-e315-43b0-98e7-405fc13840fa"
            }
        }
    },
    {
        "a": {
            "identity": 34,
            "labels": [
                "Model"
            ],
            "properties": {
                "uid": "virtual_disk",
                "editor": "xiangchao",
                "creator": "xiangchao",
                "createTime": 1617099413,
                "name": "虚拟磁盘（阵列）",
                "updateTime": 1617099413,
                "iconUrl": "",
                "uuid": "c8c132d9-19b9-4795-a968-1bc303276c1a"
            }
        }
    },
    {
        "a": {
            "identity": 36,
            "labels": [
                "Model"
            ],
            "properties": {
                "uid": "system",
                "editor": "xiangchao",
                "creator": "xiangchao",
                "createTime": 1617099443,
                "name": "操作系统",
                "updateTime": 1617099443,
                "iconUrl": "",
                "uuid": "3dd2e9ec-6678-425f-b077-976297f17020"
            }
        }
    },
    {
        "a": {
            "identity": 235,
            "labels": [
                "Model"
            ],
            "properties": {
                "editor": "xiangchao",
                "uid": "maintenance_record",
                "creator": "xiangchao",
                "createTime": 1617333249,
                "name": "硬件维修记录",
                "updateTime": 1617344966,
                "iconUrl": "",
                "uuid": "55f6b986-9946-4a11-a250-1c311964bcce"
            }
        }
    },
    {
        "a": {
            "identity": 238,
            "labels": [
                "Model"
            ],
            "properties": {
                "uid": "change_record",
                "editor": "xiangchao",
                "creator": "xiangchao",
                "createTime": 1617344511,
                "name": "硬件变动记录",
                "updateTime": 1617344974,
                "iconUrl": "",
                "uuid": "5cf1158d-9247-43a7-88f1-5936e9f319b0"
            }
        }
    }
]

data_json = json.dumps(data, indent=4, ensure_ascii=False, sort_keys=False, separators=(',', ':'))

print(type(data_json))
print(data_json)
