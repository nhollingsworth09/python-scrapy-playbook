import scrapy
from selscraper.items import UploadedVideo 

class QuotesSpider(scrapy.Spider):
    name = 'selspider'

    def start_requests(self):
        # This is dummy code with selenium. We're only using this to start the scrape. The 'parse' method will do the actual lifting.
        start_url = 'https://www.youtube.com/@JohnWatsonRooney/videos'     
        yield scrapy.Request(url=start_url, callback=self.parse)

    def parse(self, response):
        videos = response.xpath("//*[@id='content']")
        video_items = UploadedVideo()

        for video in videos:
            video_items['title'] = video.xpath(".//*[@id='video-title']/text()").get()
            video_items['views'] = video.xpath(".//*[@id='metadata-line']/span[1]/text()").get()
            video_items['when'] = video.xpath(".//*[@id='metadata-line']/span[2]/text()").get()
            
            yield video_items
            