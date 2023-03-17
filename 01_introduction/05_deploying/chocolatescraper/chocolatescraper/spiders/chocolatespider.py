# -*- coding: utf-8 -*-
"""
For our tutorial we are going to configure our Item Loader to:

- Remove the £ sign from the data we're scraping.
- Convert the scraped relative urls to full absolute urls.

We do this by using Scrapy itemloaders (preprocessors). Additionally, we'll be using pipelines to process the data before exporting by completing the below tasks:

- Convert the price from a string to a float (so we can then multiply it by the exchange rate).
- Convert the price from British Pounds to US Dollars
- Drop items that currently have no price (due to being sold out).
- Check if an Item is a duplicate and drop it if it's a duplicate.
"""

import scrapy
import http.client
from chocolatescraper.itemloaders import ChocolateProductLoader
from chocolatescraper.items import ChocolateProduct
from chocolatescraper.api_key import API_KEY

def get_proxy_url(url):
    proxy_url = f'https://api.scrapingant.com/v2/general?url={url}&x-api-key={API_KEY}'
    return proxy_url
    
conn = http.client.HTTPSConnection("api.scrapingant.com") 

class ChocolateSpider(scrapy.Spider):

   # The name of the spider
   name = 'chocolatespider'

   # These are the urls that we will start scraping
   def start_requests(self):
        start_url = 'https://www.chocolate.co.uk/collections/all'
        yield scrapy.Request(url=get_proxy_url(start_url), callback=self.parse)

   def parse(self, response):
       products = response.css('product-item')

       for product in products:
            chocolate = ChocolateProductLoader(item=ChocolateProduct(), selector=product)
            chocolate.add_css('name', "a.product-item-meta__title::text")
            chocolate.add_css('price', 'span.price', re='<span class="price">\n              <span class="visually-hidden">Sale price</span>(.*)</span>')
            chocolate.add_css('url', 'div.product-item-meta a::attr(href)')
            yield chocolate.load_item()

       #next_page = response.css('[rel="next"] ::attr(href)').get()

       if next_page is not None:
           next_page_url = 'https://www.chocolate.co.uk' + next_page
           yield response.follow(get_proxy_url(next_page_url), callback=self.parse)
           

