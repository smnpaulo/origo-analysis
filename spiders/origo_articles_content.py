# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from datetime import date, timedelta
from ast import literal_eval
import re

# reading in artice URLs as a list
with open('ItthonNagyvilagCikkek.csv','r', encoding='utf-8') as rf:
    cikkek = literal_eval(rf.read())

class Origo_Spider(scrapy.Spider):
    name = 'origo_articles'
    allowed_domains = ['origo.hu']

    def start_requests(self):
        for i in cikkek:
            yield Request(i, callback=self.parse)

    def parse(self, response):
        title_selector = '#article-head h1'
        author_selector = '.article-author ::text'
        date_selector = '#article-date'
        text_selector = '#article-text p'

        yield {
            'article_title': response.css(title_selector).extract(),
            'author' : response.css(author_selector).extract(),
            'date' : response.css(date_selector).extract(),
            'article_content': response.css(text_selector).extract(),
        }
