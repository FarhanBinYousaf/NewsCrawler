import scrapy
from ..items import NewscrawlerItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

class ExamplSpider(scrapy.Spider):
    name = 'news'
    # allowed_domains = ['example.com']
    def start_requests(self):
        urls = [
            'https://www.geo.tv/latest-news',
            'https://www.geo.tv/category/world',
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        main_div = response.css('.col-xs-6.singleBlock')
        for news in main_div:
            items = NewscrawlerItem()

            items['heading'] = news.css('.border-box .entry-title h2::text').extract_first()
            items['link'] = news.css('a::attr(href)').extract_first()
            items['date'] = news.css('.date::text').extract_first()

            # items['heading'] = heading
            # items['link'] = link
            # items['date'] = date

            yield items

        
