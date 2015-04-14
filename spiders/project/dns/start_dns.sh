#!/bin/sh
cd /usr/local/project/dns && 
/usr/local/bin/python /usr/local/project/dns/script.py && 
/usr/local/bin/scrapy crawl dns.ru