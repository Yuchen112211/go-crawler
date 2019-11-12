# -*- coding: utf-8 -*-
import scrapy
from crawler.items import CrawlerItem


class ExampleSpider(scrapy.Spider):
    name = 'bay123'
    allowed_domains = ['bay123.com/']
    start_urls = ['http://bay123.com/forum-40-1.html']

    
    def parse(self, response):

        res = response
        data = res.xpath('//div[@id="threadlist"]/div[@class="bm_c"]/form[@id="moderate"]/' + 
            'table[@id="threadlisttableid"]//tbody//th[@class="common"]')
        dataUrl = data[0].xpath('//a[@class="s xst"]')
        urls = [i.get().split('href')[1][2:] for i in dataUrl]
        urlStrs = ["bay123.com/" + urls[i] for i in range(len(urls))]
        item = CrawlerItem()
        for i in range(len(urlStrs)):
            urlSplits = urlStrs[i].split('\"')
            urlNow = urlSplits[0]
            textNow = urlSplits[-1][1:].split('<')[0]
            item['Id'] = int(res.url.split('-')[-1][:-5])*10000 + i
            item['url'] = urlNow
            item['text'] = textNow
            yield item
