# Scrapy Selenium Integration

Originally designed for automated testing of web applications, as websites became ever more Javascript heavy developers increasingly began to use Selenium for web scraping.

For years, Selenium was the most popular headless browser for web scraping (especially in Python), however, since the launch of Puppeteer and Playwright it has begun to fall out of favour.

To use Selenium in your Scrapy spiders you can use the Python Selenium library directly or else use [scrapy-selenium](https://github.com/clemfromspace/scrapy-selenium).

The first option of importing Selenium into your Scrapy spider works but isn't the cleanest implementation.

As a result, scrapy-selenium which was a Playwright style integration with Scrapy, making it much easier to use.

**Note**: However, scrapy-selenium hasn't been maintained in over 2 years.

Getting setup with Scrapy Selenium can be easy, but also a bit tricky as you need to install and configure a browser driver for **scrapy-selenium** to use.

## 1. Install Scrapy Selenium
To get started we first need to install scrapy-selenium by running the following command:

```
pip install scrapy-selenium
```

**Note**: You should use Python Version 3.6 or greater. You also need one of the Selenium compatible browsers.

## 2. Install ChromeDriver
To use scrapy-selenium you first need to have installed a Selenium compatible browser.

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
To integrate scrapy-selenium, we need to update our ```settings.py``` file with the following settings.

```
## settings.py

# for chrome driver 
from shutil import which
  
SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = which('chromedriver')
SELENIUM_DRIVER_ARGUMENTS=['--headless']  
  
DOWNLOADER_MIDDLEWARES = {
     'scrapy_selenium.SeleniumMiddleware': 800
     }
```

## 4. Update Our Spiders To Use Scrapy Selenium
Then to use Scrapy Selenium in our spiders to render the pages we want to scrape we need to change the default ```Request``` to ```SeleniumRequest``` in our spiders.

```
## settings.py
import scrapy
from selenium_demo.items import QuoteItem 
from scrapy_selenium import SeleniumRequest

class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    def start_requests(self):
        url = 'https://quotes.toscrape.com/js/'
        yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        quote_item = QuoteItem()
        for quote in response.css('div.quote'):
            quote_item['text'] = quote.css('span.text::text').get()
            quote_item['author'] = quote.css('small.author::text').get()
            quote_item['tags'] = quote.css('div.tags a.tag::text').getall()
            yield quote_item
```

Now all our requests will be made through our Splash server and any javascript on the page will be rendered.

For a deeper dive into Scrapy Selenium then be sure to check our [Scrapy Selenium guide](https://scrapeops.io/python-scrapy-playbook/scrapy-selenium/), and the [official docs](https://github.com/clemfromspace/scrapy-selenium).