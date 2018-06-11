# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from datetime import date, timedelta

start_urls = []
d1 = date(2014, 4, 01)  # start date
d2 = date(2018, 5, 27)  # end date
delta = d2 - d1
for i in range(delta.days + 1):
    curr_date = d1 + timedelta(days=i)
    start_urls.append('http://www.origo.hu/hir-archivum/'
                           + str(curr_date.year)
                           + '/'
                           + str(curr_date.year)
                           + str(curr_date.month).zfill(2)
                           + str(curr_date.day).zfill(2)
                           + '.html')

class Origo_Spider(scrapy.Spider):
    name = 'origo_meta'

    def start_requests(self):
        for i in start_urls:
            yield Request(i, callback=self.parse)


    def parse(self, response):
        element_selector = '.archive-cikk'
        url_selector = '.archive-cikk h3 a::attr(href)'
        title_selector = '.archive-cikk h3 a::attr(title)'

        for element in response.css(element_selector):
            yield {
                'article_url': element.css(url_selector).extract(),
                'article_title': element.css(title_selector).extract(),
            }
