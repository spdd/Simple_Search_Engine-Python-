# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class PositronicaItem(Item):
     name = Field()
     name2 = Field() 
     price = Field()
     img_url = Field() 		
     prod = Field()
     descr1 = Field()
     descr2 = Field()  