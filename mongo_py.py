# coding=utf-8
# Version:Python 3.8.0
# Tools:PyCharm 2020.2 x64
__date__ = '2021/4/22 13:43'
__author__ = '张勇'

from pymongo import MongoClient
import config
import time
client = MongoClient(config.host, config.port)
# 1.无权限认证
# col = client['test']['user']

# 2.权限认证
# 选择一个数据库
db = client['admin']
db.authenticate(config.username, config.password)
# 选择一个集合
col = client[config.db][config.collection]


def main():

    # print(col.find({'name': 7725510}).explain())
    print(col.find({'name': 7725510}))
    for data in col.find({'name': 7725510}):
        print(data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
