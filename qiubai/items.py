# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QiubaiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author      = scrapy.Field()
    author_logo = scrapy.Field()

    content     = scrapy.Field()
    thumb       = scrapy.Field()

    vote        = scrapy.Field()
    comments    = scrapy.Field()

