from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from detki38.items import Detki38Item
from scrapy.http import Request
from scrapy.http import HtmlResponse
from scrapy.http import TextResponse

class Detki38Spider(CrawlSpider):
    name = "detki38.ru"
    allowed_domains = ["detki38.ru"]
    start_urls = ["http://detki38.ru/allprods.php"]
    rules = (Rule(SgmlLinkExtractor(allow=('', )), callback='parse_item'),)

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//table[@class="productListing"]/tr/td[@class="productListing-data"]')
        items = []
        for site in sites:
            item = Detki38Item()
            item['name'] = site.select('a[2]/text()').extract()
            price = site.select('text()').extract()
            item['price'] = [i for i in price if not i == u'\xa0']
            item['img_url'] = site.select('a[1]/img/@src').extract()
            item['prod'] = site.select('a[2]/@href').extract()		
#            item['descr'] = site.select('dd[2]/text()').extract()
            items.append(item)
        return items
SPIDER = Detki38Spider()