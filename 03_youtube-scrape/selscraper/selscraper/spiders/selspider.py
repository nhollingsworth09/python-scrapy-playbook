import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selscraper.items import UploadedVideo 
from selscraper.driver_path import CHROMEDRIVER_PATH

class QuotesSpider(scrapy.Spider):
    name = 'selspider'

    def start_requests(self):
        # This is dummy code with selenium. We're only using this to start the scrape. The 'parse' method will do the actual lifting.
        start_url = 'https://www.youtube.com/@JohnWatsonRooney/videos'      
        yield scrapy.Request(url=start_url, callback=self.parse)

    def parse(self, response):
        video = UploadedVideo()
                
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        
        driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                                  chrome_options=chrome_options)
        
        driver.get('https://www.youtube.com/@JohnWatsonRooney/videos')
        wait = WebDriverWait(driver, 5)
        
        videos = driver.find_elements(By.CLASS_NAME, "style-scope ytd-rich-item-renderer")
        video_items = UploadedVideo()

        for video in videos:
            video_items['title'] = video.find_element(By.XPATH, './/*[@id="video-title"]').text
            video_items['views'] = video.find_element(By.XPATH, './/*[@id="metadata-line"]/span[1]').text
            video_items['when'] = video.find_element(By.XPATH, './/*[@id="metadata-line"]/span[2]').text
            
            yield video_items
            
        driver.quit()
