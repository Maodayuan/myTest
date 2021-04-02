# class LeapYear:
#     """计算某年是否为闰年"""
#     def __init__(self, year):
#         self.year = year
#
#     def answer(self):
#         year = self.year
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 # 整百年能被400整除的是闰年
#                 return '{}是闰年'.format(year)

import requests

data = {"ips": ["10.202.201.106"]}
r = requests.post("http://10.1.1.110:3001/v1/hwinventory", data=data)
print(r.text)