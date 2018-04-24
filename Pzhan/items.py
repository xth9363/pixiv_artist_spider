# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class PzhanItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    # 图的ID
    pid = scrapy.Field()
    # 作者的ID
    aid = scrapy.Field()
    p_oLink = scrapy.Field()
    artist=scrapy.Field()
    size=scrapy.Field()
    referer=scrapy.Field()
    tags = Field()




    # count=scrapy.Field() #一个作品中有张图
