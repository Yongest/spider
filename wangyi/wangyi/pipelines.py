# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
import config
import json
import time
client = MongoClient(config.host, config.port)
# 1.无权限认证
# col = client[config.db][config.collection]

# 2.权限认证
# 选择一个数据库
db = client['admin']
db.authenticate(config.username, config.password)
# 选择一个集合
col = client['test']['job']


class WangyiPipeline:
    def __init__(self):
        self.file = open('job.json', 'w')

    def process_item(self, item, spider):
        item = dict(item)
        col.insert(item)
        json_data = json.dumps(item, ensure_ascii=True)+',\n'
        self.file.write(json_data)
        return item

    def __del__(self):
        self.file.close()