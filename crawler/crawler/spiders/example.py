# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['baidu.com/']
    start_urls = ['https://www.baidu.com/']

    def parse(self, response):
    	print '---------------------'
        print response.body
    	print '---------------------'
