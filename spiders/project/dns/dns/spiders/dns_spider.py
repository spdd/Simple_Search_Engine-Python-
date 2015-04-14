# -*- coding:utf8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from dns.items import dnsItem
from scrapy.http import Request
from scrapy.http import HtmlResponse
from scrapy.http import TextResponse

class dnsSpider(CrawlSpider):
    name = "dns.ru"
    allowed_domains = ["dns-shop.ru"]
    start_urls = ["http://dns-shop.ru/irk/price_detail.php?i=%s" % i for i in range(100000,128000)]
#    rules = (Rule(SgmlLinkExtractor(allow=('price\.php', )), callback='parse_item'),)

    def parse(self, response):
#      for x in x range(100000,129000): 
#            yield Request("http://dns-shop.ru/price_detail.php?i=%s" % x, callback=self.parse_response) 
        self.log('A response from %s just arrived!' % response.url) 
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('/')
        items = []
        for site in sites:
            item = dnsItem()
            item['name'] = site.select('//h1/text()').extract()
            item['price'] = site.select('//p[2]/b/text()').extract()
            item['image_url'] = site.select('//td[@class="item_descr_image"]/a/@href').extract()
            item['prod_url'] = site.select('//p[1]/b/text()').extract()
            item['descr1'] = site.select('//td[3]/p/text()').extract()
            item['descr21'] = site.select('////*[@id="col2x"]/table[@class="prop"]//tr[2]/td[1]/text()').extract()
            item['descr22'] = site.select('////*[@id="col2x"]/table[@class="prop"]//tr[2]/td[2]/text()').extract()
            item['descr23'] = site.select('////*[@id="col2x"]/table[@class="prop"]//tr[3]/td[1]/text()').extract()
            item['descr24'] = site.select('////*[@id="col2x"]/table[@class="prop"]//tr[3]/td[2]/text()').extract()
            item['descr25'] = site.select('////*[@id="col2x"]/table[@class="prop"]//tr[4]/td[1]/text()').extract()
            item['descr26'] = site.select('////*[@id="col2x"]/table[@class="prop"]//tr[4]/td[2]/text()').extract()
            items.append(item)
        return items
SPIDER = dnsSpider()