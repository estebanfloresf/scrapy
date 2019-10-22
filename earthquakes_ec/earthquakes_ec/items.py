# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EarthquakesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Mag = scrapy.Field()
    Local_Hour = scrapy.Field()
    Latitude = scrapy.Field()
    Longitude = scrapy.Field()
    Prof = scrapy.Field()
    Region = scrapy.Field()
    Status = scrapy.Field()
    Nearest_City = scrapy.Field()
    Hour_UTC = scrapy.Field()
    LastUpdate = scrapy.Field()
