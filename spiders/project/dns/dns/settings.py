# Scrapy settings for dns project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'Mozilla/5.0 (compatible; YandexBot/3.0)'
BOT_VERSION = ''

SPIDER_MODULES = ['dns.spiders']
NEWSPIDER_MODULE = 'dns.spiders'
DEFAULT_ITEM_CLASS = 'dns.items.dnsItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
ITEM_PIPELINES = [
#	'dns.pipelines.dnsPipeline'
	'dns.pipelines.MySQLStorePipeline'
]
DEFAULT_RESPONSE_ENCODING = 'utf-8'
EXPORT_ENCODING = 'utf-8'

