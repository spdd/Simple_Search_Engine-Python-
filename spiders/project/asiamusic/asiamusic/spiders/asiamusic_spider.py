from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from asiamusic.items import AsiamusicItem
from scrapy.http import Request
from scrapy.http import HtmlResponse
from scrapy.http import TextResponse

class AsiamusicSpider(CrawlSpider):
    name = "asiamusic.ru"
    allowed_domains = ["www.asiamusic.ru"]
    start_urls = ["http://www.asiamusic.ru"]
    rules = (Rule(SgmlLinkExtractor(allow=('catalogue/default\.htm', )), callback='parse_item', follow=True),)

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//table[@cellpadding="2"]//tr[@height="98"]')
        items = []
        for site in sites:
            item = AsiamusicItem()
            item['name'] = site.select('td[2]/a/p/b/text()').extract()
            item['price'] = site.select('td[9]/a/@title').extract()
            item['img_url'] = site.select('td[1]/table//tr/td/a/@href').extract()
            item['prod'] = site.select('td[2]/a/@href').extract()
            item['descr'] = site.select('td[2]/a/text()').extract()
            items.append(item)
        return items
SPIDER = AsiamusicSpider()