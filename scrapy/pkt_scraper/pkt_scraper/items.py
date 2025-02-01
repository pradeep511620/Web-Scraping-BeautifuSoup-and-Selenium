import scrapy

class PktScraperItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    category = scrapy.Field()
    address = scrapy.Field()
    rating = scrapy.Field()
    phone = scrapy.Field()
    website = scrapy.Field()
    email = scrapy.Field()
    social_links = scrapy.Field()
    year_of_establishment = scrapy.Field()
    industry = scrapy.Field()
