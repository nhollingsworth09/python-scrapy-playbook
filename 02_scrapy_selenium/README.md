# Scrapy Selenium Integration

Originally designed for automated testing of web applications, as websites became ever more Javascript heavy developers increasingly began to use Selenium for web scraping.

For years, Selenium was the most popular headless browser for web scraping (especially in Python), however, since the launch of Puppeteer and Playwright it has begun to fall out of favour.


## 1. Install Selenium
To get started we first need to install scrapy-selenium by running the following command:

```
pip install selenium
```

**Note**: You should use Python Version 3.6 or greater. You also need one of the Selenium compatible browsers.

## 2. Install ChromeDriver
To use selenium you first need to have installed a Selenium compatible browser.

In this guide, we're going to use ChromeDiver which you can download from [here](https://chromedriver.chromium.org/downloads).

You will need to download the ChromeDriver version that matches the version of Chrome you have installed on your machine.

To find out what version you are using, go to **Settings** in your Chrome browser and then click **About Chrome** to find the version number.

![Python Scrapy Playbook - Chrome Version](https://www.digitalcitizen.life/wp-content/uploads/2019/03/chrome_version-2.png)

We should put the downloaded **chromedriver.exe** in our Scrapy project here:

```
├── scrapy.cfg
├── chromedriver.exe ## <-- Here
└── myproject
    ├── __init__.py
    ├── items.py
    ├── middlewares.py
    ├── pipelines.py
    ├── settings.py
    └── spiders
        └── __init__.py
```

## 3. Integrate Scrapy Selenium Into Project
To integrate selenium, we need to create a new middleware that handles JavaScript websites using Selenium. We need to update our ```middlewares.py```, ```settings.py```, and ```<spider>.py``` files.

### ```middlewares.py```
Inspiration from: https://stackoverflow.com/posts/31186730/revisions

Once you return that ```HtmlResponse``` (or a ```TextResponse``` if that's what you really want), Scrapy will cease processing downloaders and drop into the spider's parse method:

If it returns a Response object, Scrapy won’t bother calling any other ```process_request()``` or ```process_exception()``` methods, or the appropriate download function; it’ll return that response. The ```process_response()``` methods of installed middleware is always called on every response.

In this case, you can continue to use your spider's ```parse``` method as you normally would with HTML, except that the JS on the page has already been executed.
```
#middlewares.py

from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selscraper.driver_path import CHROMEDRIVER_PATH

WINDOW_SIZE = "1920,1080"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

class JSChromeMiddleware(object):
    def process_request(self, request, spider):
        driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                                  chrome_options=chrome_options)
        
        driver.get(request.url)
    
        body = driver.page_source
        return HtmlResponse(driver.current_url, body=body, encoding='utf-8', request=request)
```

### ```settings.py```
```
#settings.py

DOWNLOADER_MIDDLEWARES = {
    "selscraper.middlewares.JSChromeMiddleware": 430,
}
```

### ```<spider>.py```
```
#<spider>.py: Example scrapes quotes from a JS website

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

```

# Sample Project

We will be using [this](https://www.youtube.com/watch?v=lTypMlVBFM4&ab_channel=JohnWatsonRooney) video as reference for our sample project with **Scrapy + Selenium** while following [this](https://medium.com/swlh/web-scraping-with-selenium-scrapy-9d9c2e9d83b1) article for integrating the two packages.