# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # 讲师名字
    name = scrapy.Field()
    title = scrapy.Field()
    # 讲师简介
    desc = scrapy.Field()
    pass

#
# if __name__ == '__main__':
#
#     item = MyscrapyItem()
#     item['name'] = '王老师'
#     item['title'] = 'title'
#     item['desc'] = 'desc'
#     print(item)