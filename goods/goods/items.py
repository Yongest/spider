# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GoodsItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()  # 整装方案名字
    style = scrapy.Field()  # 方案风格
    src = scrapy.Field()   # 主页商品的图片
    mark = scrapy.Field()   # 主页商品的标签
    recommended_num = scrapy.Field()   # 主页商品的推荐指数
    price = scrapy.Field()   # 整装方案的价格
    vr_links = scrapy.Field()   # 整装方案的vr链接
    pass
