# -*- coding: utf-8 -*-
import scrapy
from ..items import EarthquakesItem


class GetQuakesSpider(scrapy.Spider):
    name = "get_quakes"
    allowed_domains = ["igepn.edu.ec"]
    start_urls = (
        "https://www.igepn.edu.ec/portal/eventos/www/index.html",
    )

    def parse(self, response):

        rows = response.xpath('/html/body/div[1]/div/div/table/tbody/tr')
        count = 0
        for row in rows:
            count += 1
            item = EarthquakesItem()

            item['Mag'] = str(row.xpath('.//td[2]/text()').extract_first()).strip()
            item['Local_Hour'] = str(row.xpath('.//td[4]/text()').extract_first()).strip()
            item['Latitude'] = str(row.xpath('.//td[5]/text()').extract_first()).strip()
            item['Longitude'] = str(row.xpath('.//td[6]/text()').extract_first()).strip()
            item['Prof'] = str(row.xpath('.//td[7]/text()').extract_first()).strip()
            item['Region'] = str(row.xpath('.//td[8]/text()').extract_first()).strip()
            item['Nearest_City'] = str(row.xpath('.//td[9]/text()').extract_first()).strip()
            item['Status'] = str(row.xpath('.//td[10]/text()').extract_first()).strip()
            item['Hour_UTC'] = str(row.xpath('.//td[11]/text()').extract_first()).strip()
            item['LastUpdate'] = str(row.xpath('.//td[12]/text()').extract_first()).strip()

            if str(item['Mag']) != 'None':
                yield item
            nextpage = response.xpath(
                '//*[@id="container"]/div[2]/div[2]/center/center/table[2]/tr/td[3]/a/@href').extract_first()
            lastpage = response.xpath(
                '//*[@id="container"]/div[2]/div[2]/center/center/table[2]/tr/td[4]/a/@href').extract_first()

            if nextpage:
                yield scrapy.Request(url=response.urljoin(nextpage), callback=self.parse)
            else:
                yield scrapy.Request(url=response.urljoin(lastpage), callback=self.parse)
        print(str(count) + " items generated")