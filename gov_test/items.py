# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GovTestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    provincetr = scrapy.Field()  # 省份 or 直辖市
    provincetr_code = scrapy.Field()
    city = scrapy.Field()    #城市 or
    city_code = scrapy.Field()
    county = scrapy.Field()  #区 or 县
    county_code = scrapy.Field()
    town = scrapy.Field() #街道办 or 镇
    town_code = scrapy.Field()
    village = scrapy.Field() #居委会 or 村
    village_code = scrapy.Field()

