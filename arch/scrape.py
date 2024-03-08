#!/usr/bin/env python3
import scrapy
from pathlib import Path

class BlogSpider(scrapy.Spider):
    name = 'sreality'
    start_urls = ['https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&locality_country_id=10001&per_page=500']

    def parse(self, response):
        json = response.json() 
        estates = json["_embedded"]["estates"]

        for estate in estates:
            yield {"name": estate["name"], "img": estate["_links"]["image_middle2"][0]["href"]}
        
