from scrapy.contrib.spiders import CrawlSpider, Rule
#from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from zamenika.items import ZamenikaItem
from scrapy.http import Request
from scrapy.http import HtmlResponse
from scrapy.http import TextResponse

class ZamenikaSpider(CrawlSpider):
    name = "zamenika.ru"
    allowed_domains = ["www.zamenika.ru"]
    start_urls = ["http://zamenika.ru/catalog/akkumulyatori",
                "http://zamenika.ru/catalog/filtri",
		"http://zamenika.ru/catalog/80",
		"http://zamenika.ru/catalog/98",
		"http://zamenika.ru/catalog/remni",
		"http://zamenika.ru/catalog/112"]
#    rules = (Rule(SgmlLinkExtractor(allow=('', )), callback='parse_item'),)

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//table[@id="info_table"]/tr')
        items = []
        for site in sites:
            item = ZamenikaItem()
            b = site.select('td/a/node()').extract()
	    item['name'] = [(b[i] + str(b[i+1])) for i in range(len(b)) if i % 2 == 0]	 
            item['price'] = site.select('td/td[2]/text()').extract()
#            item['img_url'] = site.select('iv[3]/table/tr/td/a/img/@src').extract()
            item['prod'] = site.select('td/a/@href').extract()		
#            item['descr'] = site.select('dd[2]/text()').extract()
            items.append(item)
        return items
SPIDER = ZamenikaSpider()