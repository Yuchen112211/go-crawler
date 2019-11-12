# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['baidu.com.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        print response
