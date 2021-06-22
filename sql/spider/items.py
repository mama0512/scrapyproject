# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 爬取内容为图书名称、图书链接、图书评论数
    title = scrapy.Field()
    link = scrapy.Field()
    comment = scrapy.Field()
