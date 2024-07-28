# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class DocItem(scrapy.Item):
    url = scrapy.Field()
    page = scrapy.Field()
    route = scrapy.Field()
    text = scrapy.Field()
