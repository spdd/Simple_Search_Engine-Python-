from scrapy import log
#from scrapy.core.exceptions import Dropitem
from twisted.enterprise import adbapi
import time
import MySQLdb.cursors
import items

R = range(200001,400000)
I = iter(R)
vendor_id = ['2']
url = ['http://irkshop.ru/']
url_pd = ['http://irkshop.ru/product.php?prod_id=']

class MySQLStorePipeline(object):

    def __init__(self):
        # @@@ hardcoded db settings
        # TODO: make settings configurable through settings
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
               db = 'irkdb',
               user = 'root',
               passwd = 'mysql',
               cursorclass = MySQLdb.cursors.DictCursor,
               charset = 'utf8',
               use_unicode = True)
    def process_item(self, spider, item):
        # run db query in thread pool
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
			url[0] + item['img_url'][0],
			0,
			'0000-00-00 00:00:00',
			0,
			0,
			0,
			0,
			0,
			url_pd[0] + item['prod_url'][0][-5:],
			item['desc1'][0],
			item['desc21'][0] + '\n' + item['desc22'][0] + '\n' + item['desc23'][0],
			item['price'][0].replace(' ',''),
			vendor_id[0],
			''))
                        log.msg("Item stored in db: %s" % item, level=log.DEBUG)

    def handle_error(self, e):
        log.err(e)
