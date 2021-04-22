# coding=utf-8
# Version:Python 3.8.0
# Tools:PyCharm 2020.2 x64
__date__ = '2021/4/22 13:43'
__author__ = '张勇'

from pymongo import MongoClient
import time
client = MongoClient(host='120.79.206.175', port=27017)
col = client['test']['user']


def main():

    print(col.find({'name': 7725510}).explain())
    # for data in col.find():
    #     print(data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
