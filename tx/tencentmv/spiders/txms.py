import scrapy
from ..items import TencentmvItem

class TxmsSpider(scrapy.Spider):
    name = 'txms'
    allowed_domains = ['v.qq.com']

    start_urls = [
        'https://v.qq.com/channel/cartoon?listpage=1&channel=cartoon&iarea=1']
    offset = 0

    def parse(self, response):
        items = TencentmvItem()
        lists = response.xpath('//div[@class="list_item"]')
        for i in lists:
            items['name'] = i.xpath('./a/@title').get()
            items['description'] = i.xpath('./div/div/@title').get()
            a = i.xpath('./a/div[@class="figure_caption"]').get()
            b=a[28:]
            items['name2']=b[0:len(b)-6]

            yield items

        if self.offset < 150:
            self.offset += 30
            url = 'https://v.qq.com/channel/cartoon?listpage=1&channel=cartoon&iarea=1'.format(
                str(self.offset))

            yield scrapy.Request(url=url, callback=self.parse)

