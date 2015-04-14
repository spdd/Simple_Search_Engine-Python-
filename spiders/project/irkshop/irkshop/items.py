# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class IrkshopItem(Item):
     name = Field()
     price = Field()		
     img_url = Field()
     prod_url = Field()
     desc1 = Field()
     desc21 = Field() 
     desc22 = Field() 
     desc23 = Field() 
