from scrapy import log
#from scrapy.core.exceptions import Dropitem
from twisted.enterprise import adbapi
import time
import MySQLdb.cursors
import items
import urllib2
from scrapy.http import HtmlResponse
from scrapy.selector import HtmlXPathSelector

R = range(1030001,1040000)
I = iter(R)
vendor_id = ['13']
url = ['http://africa.irkutsk.ru/']

def parsedesr(x):
    c = urllib2.urlopen('http://africa.irkutsk.ru/'+x)
    content = c.read()
    response = HtmlResponse(url='http://africa.irkutsk.ru/'+x, body = content, encoding="cp1251")
    hxs = HtmlXPathSelector(response=response)
    s = hxs.select('//table[2]/tr/td[2]/ul').extract()[0]
    if s == '<ul></ul>' or s == '<ul><li></ul>' or s == '<ul><li></li></ul>': 
	s = ''
	return s
    else:
    	return s

class MySQLStorePipeline(object):

    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
               host = 'localhost',
               db = 'irkdb',
               user = 'root',
               passwd = 'mysql',
               cursorclass = MySQLdb.cursors.DictCursor,
               charset = 'utf8',
               use_unicode = True)
    def process_item(self, spider, item):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)

        return item

    def _conditional_insert(self, tx, item):
                        tx.execute(\
                        "INSERT INTO `irkdb`.`search_goods` (`id`,`name`,`author`,`subsection_id`,`brand_id`,`img_url`,`img_url2`,`sef_name`,`date`,`editor`,`reason`,`views`,`forum_id`,`prod_url`,`descr`,`descr2`,`price`,`v_id`,`kupon`) "
			"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
			(I.next(),
			item['name'][0],
			0,
			4,
			1,
			''.join(url[0] + item['img_url'][0]),
			0,
			'0000-00-00 00:00:00',
			0,
			0,
			0,
			0,
			0,
			''.join(url[0] + item['prod'][0]),
			'' + parsedesr(item['prod'][0]),
			'',
			item['price'][0].split()[1],
			vendor_id[0],
			''))
                        log.msg("Item stored in db: %s" % item, level=log.DEBUG)

    def handle_error(self, e):
        log.err(e)
