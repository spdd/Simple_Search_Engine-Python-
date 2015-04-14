from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from irtoys.items import IrtoysItem
from scrapy.http import Request
from scrapy.http import HtmlResponse
from scrapy.http import TextResponse

class IrtoysSpider(CrawlSpider):
    name = "irtoys.ru"
    allowed_domains = ["www.irtoys.ru"]
    start_urls = ["http://www.irtoys.ru/"]
    rules = (Rule(SgmlLinkExtractor(allow=('index\.php', )), callback='parse_item'),)

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//div[3]/div/dl')
        items = []
        for site in sites:
            item = IrtoysItem()
            item['name'] = site.select('dd[1]/a/text()').extract()
            item['price'] = site.select('dd[3]/text()').extract()
            item['img_url'] = site.select('dt/a[1]/img/@src').extract()
            item['prod'] = site.select('dd[1]/a/@href').extract()
            item['descr'] = site.select('dd[2]/text()').extract()
            items.append(item)
        return items
SPIDER = IrtoysSpider()