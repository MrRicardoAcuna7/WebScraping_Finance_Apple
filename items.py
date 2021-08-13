# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FinanceappleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Previous_Close = scrapy.Field
    Market_Cap = scrapy.Field
    Open = scrapy.Field
    Beta = scrapy.Field
    Bid = scrapy.Field
    
    pass
