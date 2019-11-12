# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import boto3

class CrawlerPipeline(object):

	def open_spider(self, spider):
		dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
		self.table = dynamodb.Table("bay123")

	def process_item(self, item, spider):
		res = self.table.put_item (Item = dict(item))
		return item

	
