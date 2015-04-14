# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class ProdalitItem(Item):
     author = Field()
     name = Field()
     price = Field()
     img_url = Field() 		
     prod = Field()
     descr = Field()
     head1 = Field()
     head_v1 = Field()
     head2 = Field()
     head_v2 = Field()
     head3 = Field()
     head_v3 = Field()
     head4 = Field()
     head_v4 = Field()      