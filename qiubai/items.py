# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QiubaiItem(scrapy.Item):
    # define the fields for your item here like:

    author      = scrapy.Field()    # 作者
    author_logo = scrapy.Field()    # 作者头像

    content     = scrapy.Field()    # 内容
    thumb       = scrapy.Field()    # 内容图片

    vote        = scrapy.Field()    # 赞人数
    comments    = scrapy.Field()    # 评论数

