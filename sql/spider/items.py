# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()  # 标题

    price = scrapy.Field()  # 价格

    comment = scrapy.Field()  # 评价条数

    link = scrapy.Field()  # 商品链接

    info = scrapy.Field()  # 详细信息