# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class DetplanetItem(Item):
     name = Field()
     price = Field()
     img_url = Field() 		
     prod = Field()
#     descr = Field()
#     google = Field() 