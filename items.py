# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonedaItem(scrapy.Item):
    # define the fields for your item here like:
    model_name = scrapy.Field()
    model_price = scrapy.Field()
    model_ratings = scrapy.Field()
    delivery_type = scrapy.Field()


    pass
