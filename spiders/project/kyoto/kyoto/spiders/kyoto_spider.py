from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from kyoto.items import KyotoItem
from scrapy.http import Request
from scrapy.http import HtmlResponse
from scrapy.http import TextResponse

class KyotoSpider(CrawlSpider):
    name = "kyoto.ru"
    allowed_domains = ["www.kyoto.irk.ru"]
    start_urls = ["http://www.kyoto.irk.ru/index.php?cPath=0/"]
    rules = (Rule(SgmlLinkExtractor(allow=('', )), callback='parse_item'),)

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//table[1]/tr/td/table/tr[@valign="center"]')
        items = []
        for site in sites:
            item = KyotoItem()
            item['name'] = site.select('td[2]/table[1]/tr[1]/td[1]/p[1]/text()').extract()
            item['price'] = site.select('td[2]/table[1]/tr[2]/td[1]/p[1]/b/font/text()').extract()
            item['img_url'] = site.select('td[1]/a/img/@src').extract()
            item['prod'] = site.select('td[1]/a/@href').extract()		
            item['descr'] = site.select('td[2]/table[1]/tr[1]/td[1]/p[4]').extract()
            items.append(item)
        return items
SPIDER = KyotoSpider()