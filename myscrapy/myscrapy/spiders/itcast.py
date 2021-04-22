# coding=utf-8
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#ajavaee']

    def parse(self, response):
        # with open('itcast.html', 'wb') as f:
        #     f.write(response.body)
        node_list = response.xpath('//div[@class="li_txt"]')
        # print(len(node_list))
        for node in node_list:
            temp = {}
            # xpath 方法返回的是选择器对象列表、extract()用于从选择器对象中提取数据
            temp['name'] = node.xpath('./h3/text()').extract_first()
            temp['title'] = node.xpath('./h4/text()')[0].extract()
            temp['desc'] = node.xpath('./p/text()')[0].extract()
            # print(temp)
            yield temp

        pass
