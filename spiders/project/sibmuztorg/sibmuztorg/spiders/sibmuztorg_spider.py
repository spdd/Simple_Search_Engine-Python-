from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from sibmuztorg.items import SibmuztorgItem
from scrapy.http import Request
from scrapy.http import HtmlResponse
from scrapy.http import TextResponse

class SibmuztorgSpider(CrawlSpider):
    name = "sibmuztorg.ru"
    allowed_domains = ["sibmuztorg.ru"]
    start_urls = ["http://sibmuztorg.ru/"]
    rules = (Rule(SgmlLinkExtractor(allow=('', )), callback='parse_item'),)

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//table[@class="views-view-grid"]/tbody/tr/td')
        items = []
        for site in sites:
            item = SibmuztorgItem()
            item['name'] = site.select('div[@class="views-field-title"]/span/a/text()').extract()
            item['price'] = site.select('div[@class="views-field-sell-price"]/span/span[@class="uc-price-product uc-price-sell_price uc-price"]/text()').extract()
            item['img_url'] = site.select('div[@class="views-field-field-image-cache-fid"]/span/a/img/@src').extract()
            item['prod'] = site.select('div[@class="views-field-title"]/span/a/@href').extract()
            item['descr'] = site.select('div[@class="views-field-field-short-descr-value"]/div/text()').extract()
            items.append(item)
        return items
SPIDER = SibmuztorgSpider()