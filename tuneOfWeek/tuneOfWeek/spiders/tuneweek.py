# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from ..items import Tune


class TuneWeekSpider(scrapy.Spider):
    name = "tuneweek"
    allowed_domains = ["astateoftrance.com"]
    start_urls = (
        'http://www.astateoftrance.com/episodes',
    )

    def parse(self, response):
        episodes = response.xpath('//*[@id="main"]/article/h4/a/@title').extract()
        links = response.xpath('//*[@id="main"]/article/h4/a/@href').extract()
        images = response.xpath('//*[@id="main"]/article/a/img/@src').extract()
        dates = response.xpath('//*[@id="main"]/article/abbr/text()').extract()

        for episode, link, date, image in zip(episodes,links,dates,images):
            item = Tune()
            item['episode']= str(episode).strip()
            item['date'] = str(date).strip()
            item['link'] = str(link).strip()
            item['image'] = str(image).strip()
            if link:
                url = str(link).strip()
                request = Request(url=url, meta={'item': item, 'dont_merge_cookies': True}, callback=self.get_tune_week)
                request.meta['item'] = item
                yield request

    def get_tune_week(self,response):
        item = response.request.meta['item']

        try:
            tune_week = response.xpath('//*[@id="main"]/div/article[1]/div[2]/ol/li')
            if tune_week:
                for tune in tune_week:
                    artist = tune.xpath('.//strong/text()').extract_first()
                    song = tune.xpath('.//text()').extract()[1]

                    if "TUNE OF THE WEEK:" in str(artist):
                        item['artist'] = str(artist).replace("TUNE OF THE WEEK:", "").strip()
                        item['song'] = str(song).replace("– ", "").strip()
                        break
            else:
                # item['artist'] = "NA"
                # item['song'] = "NA"
                # this is because now the change to a paragraph
                tune_week = response.xpath('//*[@id="main"]/div/article[1]/div[1]//p')
                if tune_week:
                    for tune in tune_week:
                        artist = tune.xpath('strong[contains(text(),"TUNE OF THE WEEK")]/text()').extract_first()
                        if artist:
                            song = tune.xpath('.//text()').extract()[2]
                            item['artist'] = str(artist).replace("TUNE OF THE WEEK:", "").strip()
                            item['song'] = str(song).replace("– ", "").strip()
                            break



        except Exception as e:
            print(e)

        yield item

