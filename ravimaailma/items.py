# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RavimaailmaItem(scrapy.Item):
    a_url_text = scrapy.Field()
    b_url_link = scrapy.Field()
