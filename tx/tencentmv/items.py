# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentmvItem(scrapy.Item):
    # define the fields for your item here like:
     name = scrapy.Field()
     description = scrapy.Field()
     name2 = scrapy.Field()


