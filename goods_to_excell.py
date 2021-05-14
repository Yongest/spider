# coding=utf-8
# Version:Python 3.8.0
# Tools:PyCharm 2020.2 x64
__date__ = '2021/5/14 14:26'
__author__ = '张勇'
import requests
import openpyxl
import json
# f = open('./data/goods0.json',encoding='utf-8')
# print(f)
# li = json.load(f.content.decode())
# print(len(li))
domain = 'http://127.0.0.1/data/'
response = requests.get(domain+'new_goods_1.json')
json_item = json.loads(response.content.decode())
print(type(json_item))
# 创建excel
# book = openpyxl.Workbook()
# # 当前sheet
# sh = book.active
# sh.title = '商品列表'
#
# name2age = {
#     "zhangsan":19,
#     "zhangsan2":19,
#     "zhangsan3":19,
#     "zhangsan3":39,
#     "zhangsan4":192,
# }
#
# sh['A1'] = '姓名'
# sh['B1'] = '年龄'
# row = 2
# for name,age in name2age.items():
#     sh.cell(row,1).value = name
#     sh.cell(row,2).value = age
#     row+=1
# book.save('goods.xlsx')