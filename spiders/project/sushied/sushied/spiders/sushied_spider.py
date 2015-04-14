from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from sushied.items import SushiedItem
from scrapy.http import Request
from scrapy.http import HtmlResponse
from scrapy.http import TextResponse

class SushiedSpider(CrawlSpider):
    name = "sushied.ru"
    allowed_domains = ["sushied.ru"]
    start_urls = ["http://sushied.ru/page/menu"]
    rules = (Rule(SgmlLinkExtractor(allow=('', )), callback='parse_item'),)

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//div[@id="content"]/table/tr/td/div')
        items = []
        for site in sites:
            item = SushiedItem()
            item['name'] = site.select('div[1]/a/text()').extract()
            item['price'] = site.select('div[3]/div[2]/text()').extract()
            item['img_url'] = site.select('table/tr/td/div/a/img/@src').extract()
#            item['prod'] = site.select('td[1]/a/@href').extract()		
            item['descr1'] = site.select('div[3]/div[2]/text()').extract()
            item['descr2'] = site.select('div[2]/text()').extract()		
            items.append(item)
        return items
SPIDER = SushiedSpider()