from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from africa.items import AfricaItem
from scrapy.http import Request
from scrapy.http import HtmlResponse
from scrapy.http import TextResponse

class AfricaSpider(CrawlSpider):
    name = "africa.ru"
    allowed_domains = ["africa.irkutsk.ru"]
    start_urls = ["http://africa.irkutsk.ru/Velosipedi.html"]
    rules = (Rule(SgmlLinkExtractor(allow=('', )), callback='parse_item'),)

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//table[@id="t"]/tr/td')
        items = []
        for site in sites:
            item = AfricaItem()
            item['name'] = site.select('a/text()').extract()
            item['price'] = site.select('b/text()').extract()
            item['img_url'] = site.select('a/img/@src').extract()
            item['prod'] = site.select('a/@href').extract()
#            item['descr'] = site.select('dd[2]/text()').extract()
            items.append(item)
        return items
SPIDER = AfricaSpider()