# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class AmazonItem(scrapy.Item):
    productNumber = scrapy.Field()
    productAsin = scrapy.Field()
    productUuid = scrapy.Field()
    productImageLink = scrapy.Field()
    productLink = scrapy.Field()
    productTitle = scrapy.Field()
    productStar = scrapy.Field()
    numberComment = scrapy.Field()
    productPrice = scrapy.Field()
    productOldPrice = scrapy.Field()
    discountRate = scrapy.Field()