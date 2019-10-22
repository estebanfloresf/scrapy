# -*- coding: utf-8 -*-
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from ..items import ImageItem



class ImagesSpiderSpider(scrapy.Spider):
    name = 'images_spider'
    allowed_domains = ['bhid.com']
    start_urls = ['https://www.bhid.com/CatSearch/9/abrasives']

    def parse(self, response):
        # members_tag = response.css('div.categorycontent-image')
        # for member in members_tag:
        #     img_url = member.xpath("/*/a/img/@src").extract_first()
        #     img_url = 'https://www.bhid.com/'+img_url
        #     print(img_url)
        images = response.xpath('//*[@id="content"]/div/div/div[2]/div[5]/div/ul//*/a/img/@src').extract()
        for image in images:
            img_url = 'https://www.bhid.com/'+image
            yield ImageItem(image_urls=[img_url])