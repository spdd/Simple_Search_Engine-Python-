from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from prodalit.items import ProdalitItem
from scrapy.http import Request
from scrapy.http import HtmlResponse
from scrapy.http import TextResponse

class ProdalitSpider(CrawlSpider):
    name = "prodalit.ru"
    allowed_domains = ["prodalit.ru"]
    start_urls = ["http://prodalit.ru/?book=%s" % i for i in range(100000,300000)]
#    rules = (Rule(SgmlLinkExtractor(allow=('\?\catrub\=\3', )), callback='parse_item', follow=True),)

    def parse(self, response):
        self.log('A response from %s just arrived!' % response.url) 
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('/')
        items = []
        for site in sites:
            item = ProdalitItem()
            item['author'] = site.select('//table[@class="bookfull"]//td[2]/p[1]/text()').extract()
            item['name'] = site.select('//table[@class="bookfull"]//td[2]/p[2]/text()').extract()
            item['price'] = site.select('//table[@class="date"]//td[1]/span/text()').extract()
            item['img_url'] = site.select('//table[@class="bookfull"]//td[1]/img/@src').extract()
            item['prod'] = site.select('//div[@class="reg"]/form/@action').extract()
            item['descr'] = site.select('//div[@class="iinf"]/p/text()').extract()
            item['head1'] = site.select('//table[@class="date"]//tr[2]/th/text()').extract()
            item['head_v1'] = site.select('//table[@class="date"]//tr[2]/td/text()').extract()
            item['head2'] = site.select('//table[@class="date"]//tr[3]/th/text()').extract()
            item['head_v2'] = site.select('//table[@class="date"]//tr[3]/td/text()').extract()
            item['head3'] = site.select('//table[@class="date"]//tr[6]/th/text()').extract()
            item['head_v3'] = site.select('//table[@class="date"]//tr[6]/td/text()').extract()
            item['head4'] = site.select('//table[@class="date"]//tr[7]/th/text()').extract()
            item['head_v4'] = site.select('//table[@class="date"]//tr[7]/td/text()').extract()
            items.append(item)
        return items
SPIDER = ProdalitSpider()