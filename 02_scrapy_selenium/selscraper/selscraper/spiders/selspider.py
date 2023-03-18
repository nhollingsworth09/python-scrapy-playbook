import scrapy
from selscraper.items import QuoteItem 

class QuotesSpider(scrapy.Spider):
    name = 'selspider'

    def start_requests(self):
        start_url = 'https://quotes.toscrape.com/js/'      
        yield scrapy.Request(url=start_url, callback=self.parse)

    def parse(self, response):
        quote_item = QuoteItem()
        for quote in response.css('div.quote'):
            quote_item['text'] = quote.css('span.text::text').get()
            quote_item['author'] = quote.css('small.author::text').get()
            quote_item['tags'] = quote.css('div.tags a.tag::text').getall()
            yield quote_item


