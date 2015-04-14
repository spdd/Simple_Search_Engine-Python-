# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class dnsItem(Item):
     name = Field()
     price = Field()
     image_url = Field()
     prod_url = Field()
     descr1 = Field()
     descr21 = Field()
     descr22 = Field()
     descr23 = Field()
     descr24 = Field()
     descr25 = Field()
     descr26 = Field()