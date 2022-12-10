# Define here the models for your scraped items
# This is temporary container for storing the items/data etc.
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
