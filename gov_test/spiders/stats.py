# -*- coding: utf-8 -*-
import scrapy
from gov_test.items import GovTestItem
from copy import  deepcopy

class StatsSpider(scrapy.Spider):
    name = "stats"
    allowed_domains = ["stats.gov.cn"]
    start_urls = (
        'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2015/index.html',
    )

    def parse(self, response):

        for provincetr_url in  response.xpath('//tr[@class="provincetr"]/td'):
            item = GovTestItem()
            item['provincetr'] = provincetr_url.xpath('a/text()').extract()[0]
            item['provincetr_code'] = provincetr_url.xpath('a/@href').extract()[0].split('.')[0]
            provincetr_url_temp = provincetr_url.xpath('a/@href').extract()
            #yield  item
            for i in provincetr_url_temp:
                yield scrapy.Request(response.urljoin(response.url[:-10]+ i) , callback=self.parse2,meta={'item':item})

    # def parse2(self, response):
    #     for city_name in response.xpath('//tr[@class="citytr"]/td[2]'):
    #         temp = response.meta['item']
    #         # item = response.meta['item']
    #         if city_name.xpath('a/text()'):
    #             item = GovTestItem()
    #             item['city'] = city_name.xpath('a/text()').extract()[0]
    #             item['city_code'] = city_name.xpath('a/@href').extract()[0].split('.')[0].split('/')[-1]
    #             item['provincetr'] = temp['provincetr']
    #             item['provincetr_code'] = temp['provincetr_code']
    #             city_url_temp = city_name.xpath('a/@href').extract()
    #
    #             for i in city_url_temp:
    #                 yield scrapy.Request(response.urljoin(response.url[:-7] + i), callback=self.parse3,
    #                                      meta={'item': item})
    #         else:
    #             pass

    def parse2(self,response):
        for city_name in response.xpath('//tr[@class="citytr"]/td[2]'):
            item = response.meta['item']

            if city_name.xpath('a/text()'):
                item = deepcopy(item)
                item['city'] = city_name.xpath('a/text()').extract()[0]
                item['city_code'] = city_name.xpath('a/@href').extract()[0].split('.')[0].split('/')[-1]
                city_url_temp = city_name.xpath('a/@href').extract()
                #yield item
                for i in city_url_temp:
                    yield scrapy.Request(response.urljoin(response.url[:-7] + i), callback=self.parse3,meta={'item': item})

            else:
                pass

    # def parse3(self,response):
    #     for county_name in response.xpath('//tr[@class="countytr"]/td[2]'):
    #
    #         temp = response.meta['item']
    #         item = GovTestItem()
    #         if county_name.xpath('a/text()').extract():
    #             item['county'] = county_name.xpath('a/text()').extract()[0]
    #             item['county_code'] = county_name.xpath('a/@href').extract()[0].split('.')[0].split('/')[-1]
    #             item['provincetr'] = temp['provincetr']
    #             item['provincetr_code'] = temp['provincetr_code']
    #             item['city'] = temp['city']
    #             item['city_code'] = temp['city_code']
    #
    #             yield item
    #
    #         else:
    #             pass

    def parse3(self, response):
        for county_name in response.xpath('//tr[@class="countytr"]/td[2]'):
            item = response.meta['item']

            if county_name.xpath('a/text()'):
                item = deepcopy(item)
                item['county'] = county_name.xpath('a/text()').extract()[0]
                item['county_code'] = county_name.xpath('a/@href').extract()[0].split('.')[0].split('/')[-1]

                county_url_temp = county_name.xpath('a/@href').extract()
                # yield item
                for i in county_url_temp:
                    yield scrapy.Request(response.urljoin(response.url[:-9] + i),callback=self.parse4,meta={'item': item})
            else:
                pass
    def parse4(self,response):
        for town_name in response.xpath('//tr[@class="towntr"]/td[2]'):
            item = response.meta['item']
            if town_name.xpath('a/text()'):
                item = deepcopy(item)
                item['town'] = town_name.xpath('a/text()').extract()[0]
                item['town_code'] = town_name.xpath('a/@href').extract()[0].split('.')[0].split('/')[-1]
                town_url_temp = town_name.xpath('a/@href').extract()

                for i in town_url_temp:
                    yield scrapy.Request(response.urljoin(response.url[:-11] + i),callback=self.parse5,meta={'item': item})
            else:
                pass

    def parse5(self,response):
        for village_name in response.xpath('//tr[@class="villagetr"]'):
            item = response.meta['item']
            if village_name.xpath('td[3]/text()'):
                item['village'] = village_name.xpath('td[3]/text()').extract()[0]
                item['village_code'] = village_name.xpath('td[1]/text()').extract()[0].split('.')[0].split('/')[-1]
                yield item
            else:
                pass

    # def parse4(self,response):
    #     for town_name in response.xpath('//tr[@class="towntr"]/td[2]'):
    #         item = response.meta['item']
    #         if town_name.xpath('a/text()'):
    #
    #             #item = deepcopy(item)
    #             item['town'] = town_name.xpath('a/text()').extract()[0]
    #             item['town_code'] = town_name.xpath('a/@href').extract()[0].split('.')[0].split('/')[-1]
    #             yield item
    #         else:
    #             pass

        # next_pages = response.xpath('//tr[@class="provincetr"]/td/a/@href').extract()
        # for next_page in next_pages:
        #     if next_page is not None:
        #         next_page = response.urljoin(response.url[:-9]+next_page)
        #         yield scrapy.Request(next_page, callback=self.parse)
        #     else:
        #         pass


