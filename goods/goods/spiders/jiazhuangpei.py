import scrapy


class JiazhuangpeiSpider(scrapy.Spider):
    name = 'jiazhuangpei'
    allowed_domains = ['jiazhuangpei.com']
    start_urls = ['https://www.jiazhuangpei.com/combo/combo_list?type_id=1&page=1']
    print('start')

    def parse(self, response):
        print(22)
        node_list = response.xpath('//*/div')
        print(node_list)


