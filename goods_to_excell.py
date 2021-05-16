# coding=utf-8
# Version:Python 3.8.0
# Tools:PyCharm 2020.2 x64
__date__ = '2021/5/14 14:26'
__author__ = '张勇'
import requests
import openpyxl
import json
# f = open('./data/goods1.json',encoding='utf-8')
# print(f)
# li = json.load(f.content.decode())
# print(len(li))
domain = 'http://127.0.0.1/data/'
# for index in range(1,109):
response = requests.get(domain+'new_goods_77.json')
json_item = json.loads(response.content.decode())

print(len(json_item))
# 创建excel
book = openpyxl.Workbook()
# 当前sheet
sh = book.active
sh.title = '商品列表'


name_list = ["商品名字",'品牌','风格','材质','商品链接']
for index,item in enumerate(name_list):
    sh.cell(1, index+1).value = item


row = 2
for item in json_item:
    sh.cell(row,1).value = item['name']

    sh.cell(row,2).value = item['brand']
    # sh.cell(row,6).value = json.dumps(item['params'],ensure_ascii=False)
    # sh.cell(row,7).value = json.dumps(item['goods_list'],ensure_ascii=False)
    sh.cell(row, 3).value = item['sale_link_all']
    row+=1
book.save('./data/goods.xlsx')