from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from positronica.items import PositronicaItem
from scrapy.http import Request
from scrapy.http import HtmlResponse
from scrapy.http import TextResponse

class PositronicaSpider(CrawlSpider):
    name = "positronica.ru"
    allowed_domains = ["irkutsk.positronica.ru"]
    start_urls = ["http://irkutsk.positronica.ru/catalog/"]
    rules = (Rule(SgmlLinkExtractor(allow=('', )), callback='parse_item'),)

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//div[@id="catalog_list"]/div[contains(@style, "border-bottom")]')
        items = []
        for site in sites:
            item = PositronicaItem()
            item['name'] = site.select('div[2]/div[2]/a/text()').extract()
            item['name2'] = site.select('div[2]/div[2]/a/span/text()').extract()
            item['price'] = site.select('div[3]/nobr/span/text()').extract()
            item['img_url'] = site.select('div[1]/div[1]/table//tr/td/a/img/@src').extract()
            item['prod'] = site.select('div[2]/div[2]/a/@href').extract()
            item['descr1'] = site.select('div[2]/div[4]/text()').extract()
            item['descr2'] = site.select('div[2]/div[5]/text()').extract()
            items.append(item)
        return items
SPIDER = PositronicaSpider()