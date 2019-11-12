# -*- coding: utf-8 -*-
import scrapy

class ExampleSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com/']
    start_urls = ['https://www.baidu.com/s?wd=angel']

    def parse(self, response):
    	res = response
    	urlSelector = res.xpath('//div[@id="content_left"]//h3/a')
    	urls = [i.get().split('href')[1][2:] for i in urlSelector]
    	
    	for i in range(len(urls)):
    		print "URL " + str(i) + ": " + urls[i]
    		print '-----------------------------'