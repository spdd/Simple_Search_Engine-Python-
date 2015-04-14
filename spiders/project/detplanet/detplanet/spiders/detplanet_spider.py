from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from detplanet.items import DetplanetItem
from scrapy.http import Request
from scrapy.http import HtmlResponse
from scrapy.http import TextResponse

class DetplanetSpider(CrawlSpider):
    name = "det-planet.ru"
    allowed_domains = ["www.det-planet.ru"]
    start_urls = ["http://www.det-planet.ru/"]
    rules = (Rule(SgmlLinkExtractor(allow=('', )), callback='parse_item'),)

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//ul[@class="catalog_list"]/li/form[@id="form1"]')
        items = []
        for site in sites:
            item = DetplanetItem()
#            item['name'] = site.select('//div[@class="some_text_other"]/h1/text()').extract()
#            item['price'] = site.select('//div[@class="some_text_other"]/div/div[@class="text_good"]/dl/dd/text()').extract()
#            item['img_url'] = site.select('//div[@class="some_text_other"]/div/div[@class="image_good"]/a/img/@src').extract()
#            item['prod'] = site.select('//form[@id="enter"]/fieldset//input[2]/@value').extract()
#            item['descr'] = site.select('//div[@class="some_text_other"]/div[@class="inside_some_block"]/p').extract()
            item['name'] = site.select('h3/a/text()').extract()
            item['price'] = site.select('dl/dd/h4/text()').extract()
            item['img_url'] = site.select('dl/dt/a/img/@src').extract()
            item['prod'] = site.select('dl/dt/a/@href').extract()
#            item['descr'] = site.select('dd[2]/text()').extract()
            items.append(item)
        return items
SPIDER = DetplanetSpider()