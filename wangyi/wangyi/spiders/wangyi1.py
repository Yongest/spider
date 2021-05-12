import scrapy

from wangyi.items import WangyiItem


class Wangyi1Spider(scrapy.Spider):
    name = 'wangyi1'
    allowed_domains = ['hr.163.com']
    start_urls = ['https://hr.163.com/position/list.do']

    def parse(self, response):
        node_list = response.xpath('//tbody/tr')

        for num, node in enumerate(node_list):

            if num % 2 == 0:
                item = WangyiItem()
                item["name"] = node.xpath('./td[1]/a/text()').extract_first()
                item["link"] = node.xpath('./td[1]/a/@href').extract_first()
                item["department"] = node.xpath('./td[2]/text()').extract_first()
                item["category"] = node.xpath('./td[3]/text()').extract_first()
                item["type"] = node.xpath('./td[4]/text()').extract_first()
                item["address"] = node.xpath('./td[5]/text()').extract_first()
                item["num"] = node.xpath('./td[6]/text()').extract_first().strip()
                item["date"] = node.xpath('./td[7]/text()').extract_first()
                yield scrapy.Request(
                    url='https://hr.163.com'+item['link'],
                    callback=self.parse_detail,
                    meta={"item": item}
                )
        # 提取下一页的href
        next_url = response.xpath('//a[contains(text(),">")]/@href').extract_first()

        if next_url != 'javascript:void(0)':
            # 构造完整url
            url = response.urljoin(next_url)

            # 构造scrapy.Request对象，并yield给引擎
            # 利用callback参数指定该Request对象之后获取的响应用哪个函数进行解析
            yield scrapy.Request(url, callback=self.parse)

    def parse_detail(self, resposne):

        # 获取之前传入的item
        item = resposne.meta["item"]

        item['desc'] = resposne.xpath('//*[@class="section-content"][1]/text()').extract_first()
        item['require'] = resposne.xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/text()').extract()
        # print(item)
        yield item