# Scrapy settings for positronica project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'YandexBot'
BOT_VERSION = '3.0'

SPIDER_MODULES = ['positronica.spiders']
NEWSPIDER_MODULE = 'positronica.spiders'
DEFAULT_ITEM_CLASS = 'positronica.items.PositronicaItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
ITEM_PIPELINES = [
	'positronica.pipelines.MySQLStorePipeline'
]
DEFAULT_RESPONSE_ENCODING = 'utf-8'
EXPORT_ENCODING = 'utf-8'

