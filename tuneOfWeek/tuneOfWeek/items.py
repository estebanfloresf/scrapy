# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Tune(scrapy.Item):
    # define the fields for your item here like:

    episode = scrapy.Field()
    date = scrapy.Field()
    link = scrapy.Field()
    image = scrapy.Field()
    artist =  scrapy.Field()
    song = scrapy.Field()

