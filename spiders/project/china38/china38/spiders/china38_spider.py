from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from china38.items import China38Item
from scrapy.http import Request
from scrapy.http import HtmlResponse
from scrapy.http import TextResponse

class China38Spider(CrawlSpider):
    name = "china38.ru"
    allowed_domains = ["www.china38.ru"]
    start_urls = ["http://www.china38.ru/"]
    rules = (Rule(SgmlLinkExtractor(allow=('', )), callback='parse_item'),)

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//table[@id="center_table"]/tr/td[@id="c_center"]/div[@id="content"]/div[1]/div')
        items = []
        for site in sites:
            item = China38Item()
            item['name'] = site.select('div[2]/a/text()').extract()
            item['price'] = site.select('div[1]/div/text()').extract()
            item['img_url'] = site.select('div[3]/table/tr/td/a/img/@src').extract()
            item['prod'] = site.select('div[3]/table/tr/td/a/@href').extract()
#            item['descr'] = site.select('dd[2]/text()').extract()
            items.append(item)
        return items
SPIDER = China38Spider()