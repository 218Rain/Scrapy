# -*- coding: utf-8 -*-
import scrapy
from ..items import TencentItem

class TencentpositionSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']

    url = "https://hr.tencent.com/position.php?&start="
    offset = 0
    # 爬虫第一次取的url地址
    start_urls = [url + str(offset)]

    def parse(self, response):
        for each in response.xpath("//tr[@class='even']|//tr[@class='odd']"):
            item = TencentItem()

            item['positionName'] = each.xpath("./td[1]/a/text()").extract()[0]  # 职位名
            item['positionLink'] = each.xpath("./td[1]/a/@href").extract()[0]  # 详情连接
            item['positionType'] = each.xpath("./td[2]/text()").extract()  # 职位类别
            item['positionNum'] = each.xpath("./td[3]/text()").extract()[0]  # 招聘人数
            item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]  # 工作地点
            item['publishTime'] = each.xpath("./td[5]/text()").extract()[0]  # 发布时间

            # 将数据交给管道文件处理
            yield item

        if self.offset < 3050:
            self.offset += 10
        # 每次处理完一页的数据之后，重新发送下一页请求
        # 将请求重新发送给调度器入队列，出队列，交给下载器下载
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)