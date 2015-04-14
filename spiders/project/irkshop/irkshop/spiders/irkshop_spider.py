from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from irkshop.items import IrkshopItem
#from scrapy.http import Request
#from scrapy.http import HtmlResponse
#from scrapy.http import TextResponse

class IrkshopSpider(CrawlSpider):
    name = "irkshop.ru"
#    allowed_domains = ["irkshop.ru"]
    allowed_domains = ["irkshop.ru"]
#    start_urls = ["http://irkshop.ru/"]
    start_urls = ["http://irkshop.ru/product.php?prod_id=%s" % i for i in range(1,52000)]
#    rules = (Rule(SgmlLinkExtractor(allow=('product\.php', )), callback='parse_item', follow=True),)

    def parse(self, response):
        self.log('A response from %s just arrived!' % response.url) 
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('/')
        items = []
        for site in sites:
            item = IrkshopItem()
            item['name'] = site.select('//h1/text()').extract()
            item['price'] = site.select('//span[@class="price"][2]/text()').extract()
            item['img_url'] = site.select('//img[contains(@src,"product")]/@src').extract()
            item['prod_url'] = site.select('//td[@class="tovar_name"][2]/text()').extract()
            item['desc1'] = site.select('//span[@class="prod_text"]/text()').extract()
            item['desc21'] = site.select('//td[@colspan="2"][1]/ul/li[1]/text()').extract()
            item['desc22'] = site.select('//td[@colspan="2"][1]/ul/li[2]/text()').extract()
            item['desc23'] = site.select('//td[@colspan="2"][1]/ul/li[3]/text()').extract()
            items.append(item)
        return items
SPIDER = IrkshopSpider()