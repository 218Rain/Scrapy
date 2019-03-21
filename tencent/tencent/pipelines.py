# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class TencentPipeline(object):
    def __init__(self):
        self.filename = open('tencent.json', 'wb')

    def process_item(self, item, spider):
        # json.dumps()函数是将一个python数据类型列表进行json格式的编码
        # （将字典转化为字符串，序列化时对中文默认使用的ascii编码，ensure_ascii= False指定中文输出）
        text = json.dumps(dict(item), ensure_ascii= False) + '\n'
        self.filename.write(text.encode('utf-8'))
        return item

    def close_spider(self, spider):
        self.filename.close()
