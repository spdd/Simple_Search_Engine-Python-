from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from pokupok38.items import Pokupok38Item
from scrapy.http import Request
from scrapy.http import HtmlResponse
from scrapy.http import TextResponse

class Pokupok38Spider(CrawlSpider):
    name = "38pokupok.ru"
    allowed_domains = ["www.38pokupok.ru"]
    start_urls = ["http://www.38pokupok.ru/"]
    rules = (Rule(SgmlLinkExtractor(allow=('', )), callback='parse_item'),)

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//div[@id="ja-newswrap"]/div/div/div/div/div')
        items = []
        for site in sites:
            item = Pokupok38Item()
            item['name'] = site.select('div/a/text()').extract()
            item['price'] = site.select('a/span/text()').extract()
            item['img_url'] = site.select('div/div/a/img/@src').extract()
            item['prod'] = site.select('div/a/@href').extract()		
            item['descr'] = site.select('div/div[@class="smallDesc"]').extract()
            items.append(item)
        return items
SPIDER = Pokupok38Spider()